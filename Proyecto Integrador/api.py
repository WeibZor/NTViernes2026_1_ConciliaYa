from typing import Annotated

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from usuario.usuario_data import generar_datos_usuario
from usuario.HU_26_Limpieza_Usuario import limpiar_usuarios
from usuario.HU_27_Descripcion_Usuario import descripcion_usuarios
from usuario.HU_29_Query_Usuario import consultas_usuario
from usuario.HU_30_Agrupacion_Usuario import agrupaciones_usuario

app = FastAPI(
    title="ConciliaYa Data API",
    version="1.0.0",
    description="API para integrar la lógica de limpieza, exploración, simulación y análisis de Usuario con el frontend React."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

COLUMN_MAP = {
    "Id": "id",
    "Nombre": "nombre",
    "Apellido": "apellido",
    "TipoDocumento": "tipoDocumento",
    "Documento": "documento",
    "Correo": "correo",
    "Telefono": "telefono",
    "PerfilId": "perfilId",
    "Activo": "activo",
    "FechaAlta": "fechaAlta",
    "UsuarioAltaId": "usuarioAltaId",
}

USERS_STATE = None


def normalize_keys(record: dict) -> dict:
    return {COLUMN_MAP.get(key, key): value for key, value in record.items()}


def titlecase_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns={v: k for k, v in COLUMN_MAP.items()})


def serialize_df(df: pd.DataFrame):
    df_serial = df.copy()
    for columna in df_serial.columns:
        if pd.api.types.is_datetime64_any_dtype(df_serial[columna]):
            df_serial[columna] = df_serial[columna].dt.strftime("%Y-%m-%d %H:%M:%S")

    df_serial = df_serial.where(pd.notnull(df_serial), None)
    return [normalize_keys(record) for record in df_serial.to_dict(orient="records")]


def initialize_users():
    global USERS_STATE
    if USERS_STATE is None:
        df = limpiar_usuarios(generar_datos_usuario(num_registros=1000, semilla=42))
        USERS_STATE = [normalize_keys(record) for record in df.where(pd.notnull(df), None).to_dict(orient="records")]
    return USERS_STATE


def get_users_df():
    return pd.DataFrame(initialize_users())


def save_users(records: list[dict]):
    global USERS_STATE
    USERS_STATE = records


@app.get("/api/usuarios/raw")
def usuarios_raw():
    df = generar_datos_usuario(num_registros=1000, semilla=42)
    return serialize_df(df)


@app.get("/api/usuarios")
def usuarios_limpios():
    return initialize_users()


@app.post("/api/usuarios")
def crear_usuario(payload: dict):
    usuarios = initialize_users()
    next_id = max((user.get("id", 0) for user in usuarios), default=0) + 1
    nuevo = {**payload, "id": next_id}
    if "activo" not in nuevo:
        nuevo["activo"] = True
    usuarios.append(nuevo)
    save_users(usuarios)
    return nuevo


@app.put("/api/usuarios/{usuario_id}", responses={404: {"description": "Usuario no encontrado"}})
def actualizar_usuario(usuario_id: int, payload: dict):
    usuarios = initialize_users()
    usuario = next((user for user in usuarios if user["id"] == usuario_id), None)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.update(payload)
    save_users(usuarios)
    return usuario


@app.delete("/api/usuarios/{usuario_id}", responses={404: {"description": "Usuario no encontrado"}})
def eliminar_usuario(usuario_id: int):
    usuarios = initialize_users()
    usuarios_nuevos = [user for user in usuarios if user["id"] != usuario_id]
    if len(usuarios_nuevos) == len(usuarios):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    save_users(usuarios_nuevos)
    return {"message": "Usuario eliminado"}


@app.get("/api/usuarios/filter")
def usuarios_filter(
    id: Annotated[int | None, Query(None)] = None,
    activo: Annotated[bool | None, Query(None)] = None,
    perfil_id: Annotated[int | None, Query(None, alias="perfilId")] = None,
    tipo_documento: Annotated[str | None, Query(None, alias="tipoDocumento")] = None,
    search: Annotated[str | None, Query(None)] = None,
    desde_fecha_alta: Annotated[str | None, Query(None, alias="desdeFechaAlta")] = None,
):
    df = get_users_df()
    if id is not None:
        df = df[df["id"] == id]
    if activo is not None:
        df = df[df["activo"] == activo]
    if perfil_id is not None:
        df = df[df["perfilId"] == perfil_id]
    if tipo_documento is not None:
        df = df[df["tipoDocumento"].str.upper() == tipo_documento.upper()]
    if search is not None:
        pattern = search.lower()
        df = df[df.apply(lambda row: pattern in str(row["nombre"]).lower() or pattern in str(row["apellido"]).lower() or pattern in str(row["correo"]).lower(), axis=1)]
    if desde_fecha_alta is not None:
        fecha = pd.to_datetime(desde_fecha_alta, errors="coerce")
        if not pd.isna(fecha):
            df = df[pd.to_datetime(df["fechaAlta"], errors="coerce") >= fecha]
    return df.to_dict(orient="records")


@app.get("/api/usuarios/head-tail")
def usuarios_head_tail():
    df = get_users_df()
    return {
        "head": df.head(5).to_dict(orient="records"),
        "tail": df.tail(5).to_dict(orient="records"),
    }


@app.get("/api/usuarios/summary")
def usuarios_summary():
    df = titlecase_columns(get_users_df())
    desc = descripcion_usuarios(df)
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "categorical_columns": desc["categoricas"],
        "numeric_columns": desc["numericas"],
        "sample": {
            "head": serialize_df(df.head(5)),
            "tail": serialize_df(df.tail(5)),
        },
    }


@app.get("/api/usuarios/queries")
def usuarios_queries():
    df = titlecase_columns(get_users_df())
    resultados = consultas_usuario(df)
    return {key: serialize_df(value) for key, value in resultados.items()}


@app.get("/api/usuarios/groupings")
def usuarios_groupings():
    df = titlecase_columns(get_users_df())
    agrupaciones = agrupaciones_usuario(df)
    return {key: serialize_df(value) for key, value in agrupaciones.items()}


@app.get("/api/usuarios/stats")
def usuarios_stats():
    df = titlecase_columns(get_users_df())
    agrupaciones = agrupaciones_usuario(df)
    return {    
        "totalUsuarios": len(df),
        "perfiles": agrupaciones["por_perfil_activo"].to_dict(orient="records"),
        "tiposDocumento": agrupaciones["por_tipo_documento"].to_dict(orient="records"),
    }

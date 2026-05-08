from typing import Any, Dict, List, Optional

from fastapi import FastAPI, Query, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from usuario.usuario_data import generar_datos_usuario
from usuario.HU_26_Limpieza_Usuario import limpiar_usuarios
from usuario.HU_27_Descripcion_Usuario import descripcion_usuarios
from usuario.HU_29_Query_Usuario import consultas_usuario
from usuario.HU_30_Agrupacion_Usuario import agrupaciones_usuario

from tipoconflicto.tipoconflicto_data import generar_datos_tipoconflicto
from tipoconflicto.HU_21_Limpieza_TipoConflicto import limpiar_tipos_conflicto
from tipoconflicto.HU_22_Descripcion_TipoConflicto import descripcion_tipos_conflicto
from tipoconflicto.HU_24_Query_TipoConflicto import consultas_tipos_conflicto
from tipoconflicto.HU_25_Agrupacion_TipoConflicto import agrupaciones_tipos_conflicto

app = FastAPI(
    title="ConciliaYa Data API",
    version="1.0.0",
    description="API para integrar la lógica de limpieza, exploración, simulación y análisis de Usuario y TipoConflicto con el frontend React."
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

TIPOCONFLICTO_COLUMN_MAP = {
    "Id": "id",
    "Nombre": "nombre",
    "Descripcion": "descripcion",
    "Activo": "activo",
    "FechaAlta": "fechaAlta",
    "UsuarioAltaId": "usuarioAltaId",
}

USERS_STATE = None

TIPOCONFLICTO_STATE = None


def normalize_keys(record: dict, column_map: dict) -> dict:
    return {column_map.get(key, key): value for key, value in record.items()}


def titlecase_columns(df: pd.DataFrame, column_map: dict) -> pd.DataFrame:
    reverse_map = {v: k for k, v in column_map.items()}
    return df.rename(columns=reverse_map)


def serialize_df(df: pd.DataFrame, column_map: dict):
    df_serial = df.copy()
    for columna in df_serial.columns:
        if pd.api.types.is_datetime64_any_dtype(df_serial[columna]):
            df_serial[columna] = df_serial[columna].dt.strftime("%Y-%m-%d %H:%M:%S")

    df_serial = df_serial.where(pd.notnull(df_serial), None)
    return [normalize_keys(record, column_map) for record in df_serial.to_dict(orient="records")]


def initialize_users():
    global USERS_STATE
    if USERS_STATE is None:
        df = limpiar_usuarios(generar_datos_usuario(num_registros=1000, semilla=42))
        USERS_STATE = [normalize_keys(record, COLUMN_MAP) for record in df.where(pd.notnull(df), None).to_dict(orient="records")]
    return USERS_STATE


def initialize_tipoconflictos():
    global TIPOCONFLICTO_STATE
    if TIPOCONFLICTO_STATE is None:
        df = limpiar_tipos_conflicto(generar_datos_tipoconflicto(num_registros=1000, semilla=42))
        TIPOCONFLICTO_STATE = [normalize_keys(record, TIPOCONFLICTO_COLUMN_MAP) for record in df.where(pd.notnull(df), None).to_dict(orient="records")]
    return TIPOCONFLICTO_STATE


def get_users_df():
    return pd.DataFrame(initialize_users())


def save_users(records: List[Dict[str, Any]]):
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
def crear_usuario(payload: Dict[str, Any]):
    usuarios = initialize_users()
    next_id = max((user.get("id", 0) for user in usuarios), default=0) + 1
    nuevo = {**payload, "id": next_id}
    if "activo" not in nuevo:
        nuevo["activo"] = True
    usuarios.append(nuevo)
    save_users(usuarios)
    return nuevo


@app.put("/api/usuarios/{usuario_id}", responses={404: {"description": "Usuario no encontrado"}})
def actualizar_usuario(usuario_id: int, payload: Dict[str, Any]):
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
    id: Optional[int] = Query(default=None),
    activo: Optional[bool] = Query(default=None),
    perfil_id: Optional[int] = Query(default=None, alias="perfilId"),
    tipo_documento: Optional[str] = Query(default=None, alias="tipoDocumento"),
    search: Optional[str] = Query(default=None),
    desde_fecha_alta: Optional[str] = Query(default=None, alias="desdeFechaAlta"),
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


@app.get("/api/tipoconflictos/raw")
def tipoconflictos_raw():
    df = generar_datos_tipoconflicto(num_registros=1000, semilla=42)
    return serialize_df(df, TIPOCONFLICTO_COLUMN_MAP)


@app.get("/api/tipoconflictos")
def tipoconflictos_limpios():
    return initialize_tipoconflictos()


@app.get("/api/tipoconflictos/summary")
def tipoconflictos_summary():
    df = titlecase_columns(pd.DataFrame(initialize_tipoconflictos()), TIPOCONFLICTO_COLUMN_MAP)
    desc = descripcion_tipos_conflicto(df)
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "categorical_columns": desc["categoricas"],
        "numeric_columns": desc["numericas"],
        "sample": {
            "head": serialize_df(df.head(5), TIPOCONFLICTO_COLUMN_MAP),
            "tail": serialize_df(df.tail(5), TIPOCONFLICTO_COLUMN_MAP),
        },
    }


@app.get("/api/tipoconflictos/queries")
def tipoconflictos_queries():
    df = titlecase_columns(pd.DataFrame(initialize_tipoconflictos()), TIPOCONFLICTO_COLUMN_MAP)
    resultados = consultas_tipos_conflicto(df)
    return {key: serialize_df(value, TIPOCONFLICTO_COLUMN_MAP) for key, value in resultados.items()}


@app.get("/api/tipoconflictos/groupings")
def tipoconflictos_groupings():
    df = titlecase_columns(pd.DataFrame(initialize_tipoconflictos()), TIPOCONFLICTO_COLUMN_MAP)
    agrupaciones = agrupaciones_tipos_conflicto(df)
    return {key: serialize_df(value, TIPOCONFLICTO_COLUMN_MAP) for key, value in agrupaciones.items()}


@app.post("/api/tipoconflictos/simulate")
def simulate_tipoconflictos(num_registros: int = Body(default=1000, embed=True)):
    global TIPOCONFLICTO_STATE
    df = limpiar_tipos_conflicto(generar_datos_tipoconflicto(num_registros=num_registros, semilla=42))
    TIPOCONFLICTO_STATE = [normalize_keys(record, TIPOCONFLICTO_COLUMN_MAP) for record in df.where(pd.notnull(df), None).to_dict(orient="records")]
    return {"message": f"Simulados {len(TIPOCONFLICTO_STATE)} tipos de conflicto", "data": TIPOCONFLICTO_STATE}


@app.post("/api/tipoconflictos/clean")
def clean_tipoconflictos():
    global TIPOCONFLICTO_STATE
    df = pd.DataFrame(TIPOCONFLICTO_STATE)
    df_titlecase = titlecase_columns(df, TIPOCONFLICTO_COLUMN_MAP)
    df_clean = limpiar_tipos_conflicto(df_titlecase)
    TIPOCONFLICTO_STATE = [normalize_keys(record, TIPOCONFLICTO_COLUMN_MAP) for record in df_clean.where(pd.notnull(df_clean), None).to_dict(orient="records")]
    return {"message": f"Limpieza completada, {len(TIPOCONFLICTO_STATE)} registros", "data": TIPOCONFLICTO_STATE}


@app.get("/api/tipoconflictos/queries/{query_type}")
def get_tipoconflictos_queries(query_type: str):
    df = titlecase_columns(pd.DataFrame(initialize_tipoconflictos()), TIPOCONFLICTO_COLUMN_MAP)
    resultados = consultas_tipos_conflicto(df)
    if query_type in resultados:
        return serialize_df(resultados[query_type], TIPOCONFLICTO_COLUMN_MAP)
    return {"error": "Query type not found"}


@app.get("/api/tipoconflictos/groupings/{group_type}")
def get_tipoconflictos_groupings(group_type: str):
    df = titlecase_columns(pd.DataFrame(initialize_tipoconflictos()), TIPOCONFLICTO_COLUMN_MAP)
    agrupaciones = agrupaciones_tipos_conflicto(df)
    if group_type in agrupaciones:
        return serialize_df(agrupaciones[group_type], TIPOCONFLICTO_COLUMN_MAP)
    return {"error": "Group type not found"}


@app.post("/api/tipoconflictos")
def crear_tipoconflicto(payload: Dict[str, Any]):
    tipos = initialize_tipoconflictos()
    next_id = max((t.get("id", 0) for t in tipos), default=0) + 1
    nuevo = {**payload, "id": next_id}
    if "activo" not in nuevo:
        nuevo["activo"] = True
    tipos.append(nuevo)
    TIPOCONFLICTO_STATE[:] = tipos
    return nuevo


@app.put("/api/tipoconflictos/{tipo_id}")
def actualizar_tipoconflicto(tipo_id: int, payload: Dict[str, Any]):
    tipos = initialize_tipoconflictos()
    tipo = next((t for t in tipos if t["id"] == tipo_id), None)
    if tipo is None:
        raise HTTPException(status_code=404, detail="Tipo de conflicto no encontrado")

    tipo.update(payload)
    TIPOCONFLICTO_STATE[:] = tipos
    return tipo


@app.delete("/api/tipoconflictos/{tipo_id}")
def eliminar_tipoconflicto(tipo_id: int):
    tipos = initialize_tipoconflictos()
    tipos_nuevos = [t for t in tipos if t["id"] != tipo_id]
    if len(tipos_nuevos) == len(tipos):
        raise HTTPException(status_code=404, detail="Tipo de conflicto no encontrado")

    TIPOCONFLICTO_STATE[:] = tipos_nuevos
    return {"message": "Tipo de conflicto eliminado"}


@app.get("/api/tipoconflictos/filter")
def tipoconflictos_filter(
    id: Optional[int] = Query(default=None),
    activo: Optional[bool] = Query(default=None),
    search: Optional[str] = Query(default=None),
):
    df = pd.DataFrame(initialize_tipoconflictos())
    if id is not None:
        df = df[df["id"] == id]
    if activo is not None:
        df = df[df["activo"] == activo]
    if search is not None:
        pattern = search.lower()
        df = df[df.apply(lambda row: pattern in str(row["nombre"]).lower() or pattern in str(row["descripcion"]).lower(), axis=1)]
    return df.to_dict(orient="records")

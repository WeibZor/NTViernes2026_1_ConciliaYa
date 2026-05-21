import pandas as pd

def limpiar_perfil(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpieza de textos
    df_limpio["nombre"] = df_limpio["nombre"].astype("string").str.strip().str.lower()
    df_limpio["descripcion"] = df_limpio["descripcion"].astype("string").str.strip()

    # 2. Controlar valores inesperados (Nombres de personas o textos de error)
    valores_esperados_nombre = ["administrador", "gestor", "usuario"]
    df_limpio["nombre"] = df_limpio["nombre"].where(
        df_limpio["nombre"].isin(valores_esperados_nombre),
        pd.NA
    )

    valores_invalidos_desc = ["no hay acceso", "no tienes permiso", "no te dejo entrar"]
    df_limpio["descripcion"] = df_limpio["descripcion"].where(
        ~df_limpio["descripcion"].str.lower().isin(valores_invalidos_desc),
        pd.NA
    )

    # 3. Limpieza de numéricos y booleanos
    df_limpio["id"] = pd.to_numeric(df_limpio["id"], errors='coerce')
    df_limpio["activo"] = df_limpio["activo"].map({True: True, False: False, 1: True, 0: False})

    # Validar rangos numéricos de ID (eliminando los errores 0 y -1)
    df_limpio = df_limpio[df_limpio["id"] > 0]

    # 4. Limpieza de Fechas
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"], errors='coerce')
    fecha_default = pd.to_datetime("2026-01-01")
    df_limpio["fecha"] = df_limpio["fecha"].fillna(fecha_default)

    # 5. Descartar filas con vacíos en columnas obligatorias
    columnas_obligatorias = ["id", "nombre", "descripcion", "activo", "fecha"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    return df_limpio
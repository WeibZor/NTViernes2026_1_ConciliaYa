import pandas as pd

def limpiar_mediacion(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpieza de textos
    df_limpio["Lugar"] = df_limpio["Lugar"].astype("string").str.strip()
    df_limpio["Observaciones"] = df_limpio["Observaciones"].astype("string").str.strip()
    df_limpio["Resultado"] = df_limpio["Resultado"].astype("string").str.strip()

    # Controlar lugares inválidos del simulador
    valores_invalidos_lugar = ["LugarFalso1", "LugarFalso2"]
    df_limpio["Lugar"] = df_limpio["Lugar"].where(
        ~df_limpio["Lugar"].isin(valores_invalidos_lugar),
        pd.NA
    )

    # 2. Limpieza de datos numéricos
    df_limpio["Id"] = pd.to_numeric(df_limpio["Id"], errors='coerce')
    df_limpio["ConflictoId"] = pd.to_numeric(df_limpio["ConflictoId"], errors='coerce')
    df_limpio["UsuarioMediadorId"] = pd.to_numeric(df_limpio["UsuarioMediadorId"], errors='coerce')
    df_limpio["Activo"] = df_limpio["Activo"].map({True: True, False: False, 1: True, 0: False})

    # Verificar valores numéricos esperados
    df_limpio = df_limpio[df_limpio["Id"] > 0]
    df_limpio = df_limpio[df_limpio["ConflictoId"] > 0]

    # 3. Limpieza de Fechas
    df_limpio["FechaProgramada"] = pd.to_datetime(df_limpio["FechaProgramada"], errors='coerce')
    df_limpio["FechaRegistro"] = pd.to_datetime(df_limpio["FechaRegistro"], errors='coerce')

    fecha_default = pd.to_datetime("2026-03-25")
    df_limpio["FechaProgramada"] = df_limpio["FechaProgramada"].fillna(fecha_default)

    # 4. Descartar filas vacías en campos clave obligatorios
    columnas_obligatorias = ["Id", "ConflictoId", "UsuarioMediadorId", "Lugar"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    return df_limpio
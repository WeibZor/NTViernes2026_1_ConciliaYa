import pandas as pd

def limpiar_conflicto(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpieza de textos
    df_limpio["Asunto"] = df_limpio["Asunto"].astype("string").str.strip()
    df_limpio["Descripcion"] = df_limpio["Descripcion"].astype("string").str.strip()
    df_limpio["Resultado"] = df_limpio["Resultado"].astype("string").str.strip()

    # Controlar valores corruptos del simulador
    df_limpio["Asunto"] = df_limpio["Asunto"].where(
        ~df_limpio["Asunto"].isin(["Asunto_Invalido", "TEST_ERROR"]),
        pd.NA
    )

    # 2. Limpieza de datos numéricos y booleanos
    df_limpio["Id"] = pd.to_numeric(df_limpio["Id"], errors='coerce')
    df_limpio["UsuarioDemandanteId"] = pd.to_numeric(df_limpio["UsuarioDemandanteId"], errors='coerce')
    df_limpio["UsuarioDemandadoId"] = pd.to_numeric(df_limpio["UsuarioDemandadoId"], errors='coerce')
    df_limpio["MontoReclamado"] = pd.to_numeric(df_limpio["MontoReclamado"], errors='coerce')
    df_limpio["Activo"] = df_limpio["Activo"].map({True: True, False: False, 1: True, 0: False})

    # Verificar que las ID y Montos esperados cumplan las reglas de negocio
    df_limpio = df_limpio[df_limpio["Id"] > 0]
    df_limpio = df_limpio[df_limpio["UsuarioDemandanteId"] > 0]
    df_limpio = df_limpio[df_limpio["MontoReclamado"] >= 1000.00]

    # 3. Limpieza de Fechas
    df_limpio["FechaInicio"] = pd.to_datetime(df_limpio["FechaInicio"], errors='coerce')
    df_limpio["FechaCierre"] = pd.to_datetime(df_limpio["FechaCierre"], errors='coerce') # Puede ser NULL
    df_limpio["FechaAlta"] = pd.to_datetime(df_limpio["FechaAlta"], errors='coerce')

    fecha_default = pd.to_datetime("2026-03-20")
    df_limpio["FechaInicio"] = df_limpio["FechaInicio"].fillna(fecha_default)

    # 4. Descartar filas con nulos en columnas obligatorias
    columnas_obligatorias = ["Id", "UsuarioDemandanteId", "UsuarioDemandadoId", "Asunto", "FechaInicio"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    return df_limpio
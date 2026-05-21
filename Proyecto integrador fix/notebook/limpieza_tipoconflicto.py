import pandas as pd

def limpiar_tipoConflicto(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpieza de textos
    df_limpio["Nombre"] = df_limpio["Nombre"].astype("string").str.strip().str.lower()
    df_limpio["Descripcion"] = df_limpio["Descripcion"].astype("string").str.strip()

    # 2. Controlar valores esperados en Nombre
    valores_esperados_nombre = ["pago", "contrato", "servicio"]
    df_limpio["Nombre"] = df_limpio["Nombre"].where(
        df_limpio["Nombre"].isin(valores_esperados_nombre),
        pd.NA
    )

    # 3. Limpieza de datos numéricos y booleanos
    df_limpio["Id"] = pd.to_numeric(df_limpio["Id"], errors='coerce')
    
    # Mapea y filtra booleanos verdaderos descartando strings sucios como "123"
    df_limpio["Activo"] = df_limpio["Activo"].map({True: True, False: False, 1: True, 0: False})

    # Verificar rango de ID
    df_limpio = df_limpio[df_limpio["Id"] > 0]

    # 4. Descartar filas con nulos en columnas obligatorias (Sin fechas aquí)
    columnas_obligatorias = ["Id", "Nombre", "Descripcion", "Activo"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    return df_limpio
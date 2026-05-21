import pandas as pd

def limpiar_estadoConflictos(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpieza de textos (Minúsculas en nombre y código)
    df_limpio["nombre"] = df_limpio["nombre"].astype("string").str.strip().str.lower()
    df_limpio["codigo"] = df_limpio["codigo"].astype("string").str.strip().str.upper()
    df_limpio["descripcion"] = df_limpio["descripcion"].astype("string").str.strip()

    # 2. Controlar valores inesperados inyectados ("MedioCerrado", "MedioAbierto")
    valores_esperados_nombre = ["abierto", "cerrado", "proceso"]
    df_limpio["nombre"] = df_limpio["nombre"].where(
        df_limpio["nombre"].isin(valores_esperados_nombre),
        pd.NA
    )

    valores_esperados_codigo = ["ABR001", "CER002", "PRO003"]
    df_limpio["codigo"] = df_limpio["codigo"].where(
        df_limpio["codigo"].isin(valores_esperados_codigo),
        pd.NA
    )

    # 3. Limpieza de datos numéricos y lógicos (El simulador guardó "True"/"False" como texto)
    df_limpio["id"] = pd.to_numeric(df_limpio["id"], errors='coerce')
    
    # Convertimos los strings "True"/"False" o booleanos reales a booleano de pandas
    df_limpio["estado"] = df_limpio["estado"].astype(str).str.strip().str.lower().map({"true": True, "false": False})

    # Verificar ID válidos esperados en el rango (eliminando el error de id=1000)
    df_limpio = df_limpio[(df_limpio["id"] > 0) & (df_limpio["id"] <= 100)]

    # 4. Columnas obligatorias (Sin fechas aquí)
    columnas_obligatorias = ["id", "nombre", "codigo", "estado"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    return df_limpio
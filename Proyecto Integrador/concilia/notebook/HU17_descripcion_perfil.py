import pandas as pd


def descripcion_perfil(df):
    """HU 17: Describe la tabla Perfil para entender su estructura y calidad."""
    print("\n[HU 17] Descripción exploratoria con Pandas")
    print("\n--- Muestra inicial (head) ---")
    print(df.head(5))

    print("\n--- Muestra final (tail) ---")
    print(df.tail(5))

    print("\n--- Estructura del DataFrame ---")
    df.info()

    print("\n--- Estadísticas descriptivas numéricas ---")
    print(df.describe(include=["number"]))

    print("\n--- Estadísticas descriptivas categóricas / booleanas ---")
    print(df.describe(include=["object", "string", "boolean"]))

    print(f"\nCantidad de filas: {df.shape[0]}")
    print(f"Cantidad de columnas: {df.shape[1]}")
    print(f"Nombres de variables: {list(df.columns)}")

    categoricas = df.select_dtypes(include=["object", "string", "boolean"]).columns.tolist()
    numericas = df.select_dtypes(include=["number", "datetime64[ns]"]).columns.tolist()
    print(f"Columnas categóricas: {categoricas}")
    print(f"Columnas numéricas/fecha: {numericas}")

    return {
        "categoricas": categoricas,
        "numericas": numericas,
        "filas": df.shape[0],
        "columnas": df.shape[1],
    }
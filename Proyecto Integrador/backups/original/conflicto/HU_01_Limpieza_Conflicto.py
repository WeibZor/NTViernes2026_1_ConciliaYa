import pandas as pd


def limpiar_conflictos(df):
    """HU 01: Limpia la tabla Conflicto y documenta las transformaciones."""
    df_limpio = df.copy()
    print("\n[HU 01] Limpieza del set de datos")

    nulos = df_limpio.isna().sum()
    print("Nulos por columna:\n", nulos)

    columnas_texto = [col for col in df_limpio.columns if df_limpio[col].dtype == object]
    for col in columnas_texto:
        df_limpio[col] = (
            df_limpio[col]
            .astype("string")
            .str.strip()
            .replace({"<NA>": pd.NA})
        )

    for col in df_limpio.columns:
        if col.lower().endswith("id"):
            df_limpio[col] = pd.to_numeric(df_limpio[col], errors="coerce").astype("Int64")

    if "Fecha" in " ".join(df_limpio.columns):
        for col in df_limpio.columns:
            if "fecha" in col.lower():
                df_limpio[col] = pd.to_datetime(df_limpio[col], errors="coerce")

    if "Activo" in df_limpio.columns:
        df_limpio["Activo"] = df_limpio["Activo"].astype("boolean")

    antes = len(df_limpio)
    df_limpio = df_limpio.drop_duplicates()
    df_limpio = df_limpio.dropna(how="all")
    despues = len(df_limpio)

    print(f"Registros antes: {antes}, después: {despues}")
    print(
        "Transformaciones aplicadas: detección de nulos, eliminación de duplicados, corrección de tipos y normalización de texto."
    )
    return df_limpio

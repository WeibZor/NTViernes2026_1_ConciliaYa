import pandas as pd


def limpiar_tipos_conflicto(df):
    """HU 21: Limpia la tabla TipoConflicto y documenta las transformaciones."""
    df_limpio = df.copy()
    print("\n[HU 21] Limpieza del set de datos")

    nulos = df_limpio.isna().sum()
    print("Nulos por columna:\n", nulos)

    columnas_texto = ["Nombre", "Descripcion"]
    for col in columnas_texto:
        if col in df_limpio.columns:
            df_limpio[col] = (
                df_limpio[col]
                .astype("string")
                .str.strip()
                .replace({"<NA>": pd.NA})
            )

    if "Nombre" in df_limpio.columns:
        df_limpio["Nombre"] = df_limpio["Nombre"].str.title()

    df_limpio["Id"] = pd.to_numeric(df_limpio["Id"], errors="coerce")
    df_limpio["Activo"] = df_limpio["Activo"].astype("boolean")
    df_limpio["FechaAlta"] = pd.to_datetime(
        df_limpio["FechaAlta"], errors="coerce", format="%Y-%m-%d %H:%M:%S"
    )
    df_limpio["UsuarioAltaId"] = pd.to_numeric(df_limpio["UsuarioAltaId"], errors="coerce").astype("Int64")

    antes = len(df_limpio)
    df_limpio = df_limpio.drop_duplicates()
    df_limpio = df_limpio.dropna(
        subset=["Id", "Nombre", "Activo", "FechaAlta"]
    )
    df_limpio = df_limpio[df_limpio["Id"] > 0]
    despues = len(df_limpio)

    print(f"Registros antes: {antes}, después: {despues}")
    print(
        "Transformaciones aplicadas: eliminación de duplicados, corrección de tipos, normalización de texto y eliminación de registros incompletos."
    )
    return df_limpio
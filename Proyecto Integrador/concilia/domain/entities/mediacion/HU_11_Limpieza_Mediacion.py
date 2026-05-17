import pandas as pd


def limpiar_mediaciones(data_frame):
    """Limpia la tabla Mediacion y reporta transformaciones realizadas."""
    df = data_frame.copy()
    transformaciones = []

    # Normalizar texto
    columnas_texto = [
        "lugar",
        "observaciones",
        "resultado",
        "estado"
    ]
    for columna in columnas_texto:
        if columna in df.columns:
            df[columna] = (
                df[columna]
                .astype("string")
                .str.strip()
                .replace({r"\s+": " ", r"^\s+|\s+$": ""}, regex=True)
            )
            transformaciones.append(f"Normalizada columna {columna}")

    # Corrección de tipos de datos
    columnas_int = ["id", "conflicto_id", "usuario_mediador_id", "estado_conflicto_id"]
    for columna in columnas_int:
        if columna in df.columns:
            df[columna] = pd.to_numeric(df[columna], errors="coerce").astype("Int64")
            transformaciones.append(f"Convertida columna {columna} a entero seguro")

    if "fecha_programada" in df.columns:
        df["fecha_programada"] = pd.to_datetime(
            df["fecha_programada"], errors="coerce"
        )
        transformaciones.append("Convertida columna fecha_programada a datetime")

    if "fecha_registro" in df.columns:
        df["fecha_registro"] = pd.to_datetime(
            df["fecha_registro"], errors="coerce"
        )
        transformaciones.append("Convertida columna fecha_registro a datetime")

    if "costo" in df.columns:
        df["costo"] = pd.to_numeric(df["costo"], errors="coerce")
        transformaciones.append("Convertida columna costo a numérica")

    # Reporte de valores nulos por columna
    reporte_nulos = df.isna().sum().to_dict()

    # Eliminar duplicados exactos
    antes = len(df)
    df = df.drop_duplicates()
    despues = len(df)
    transformaciones.append(f"Eliminados {antes - despues} duplicados exactos")

    # Eliminar filas con identificadores faltantes o inválidos
    columnas_obligatorias = ["id", "conflicto_id", "usuario_mediador_id", "estado", "fecha_registro"]
    columnas_existentes = [c for c in columnas_obligatorias if c in df.columns]
    if columnas_existentes:
        df = df.dropna(subset=columnas_existentes)
        transformaciones.append(
            f"Eliminadas filas con valores nulos en columnas obligatorias: {', '.join(columnas_existentes)}"
        )

    resultado = {
        "data_frame": df,
        "reporte_nulos": reporte_nulos,
        "transformaciones": transformaciones,
        "columnas_mantenimiento": df.columns.tolist()
    }
    return resultado

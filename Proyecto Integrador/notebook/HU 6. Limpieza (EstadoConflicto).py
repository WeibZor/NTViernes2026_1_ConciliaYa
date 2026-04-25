import pandas as pd


def limpiar_estadosConflictos(data_frame):

    data_frame_limpio = data_frame.copy()

    # limpiar espacios en blanco en columnas de texto
    datos_texto = ["nombre", "codigo", "estado", "descripcion"]

    for columna in datos_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
        )

    # definir valores permitidos
    nombres_validos = ["abierto", "cerrado", "Proceso"]

    data_frame_limpio["nombre"] = (
        data_frame_limpio["nombre"]
        .where(
            data_frame_limpio["nombre"]
            .isin(nombres_validos),
            pd.NA
        )
    )

    codigos_validos = ["ABR001", "CER002", "PRO003"]

    data_frame_limpio["codigo"] = (
        data_frame_limpio["codigo"]
        .where(
            data_frame_limpio["codigo"]
            .isin(codigos_validos),
            pd.NA
        )
    )

    estados_validos = ["True", "False"]

    data_frame_limpio["estado"] = (
        data_frame_limpio["estado"]
        .where(
            data_frame_limpio["estado"]
            .isin(estados_validos),
            pd.NA
        )
    )

    # convertir columna numérica
    data_frame_limpio["id"] = pd.to_numeric(
        data_frame_limpio["id"],
        errors="coerce"
    )

    # eliminar filas con datos obligatorios vacíos
    columnas_obligatorias = [
        "id",
        "nombre",
        "codigo",
        "estado",
        "descripcion"
    ]

    data_frame_limpio = data_frame_limpio.dropna(
        subset=columnas_obligatorias
    )

    # eliminar valores inválidos
    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["id"] > 0
    ]

    # eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
import pandas as pd


def limpiar_simulacion(data_frame):


    data_frame_limpio = data_frame.copy()


    # limpiar espacios en blanco en columnas de texto
    datos_texto = ["servicio", "codigo"]


    for columna in datos_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
        )


    # definir valores permitidos
    servicios_validos = [
        "esterilizacion",
        "corte uñas",
        "vacunacion"
    ]


    data_frame_limpio["servicio"] = (
        data_frame_limpio["servicio"]
        .where(
            data_frame_limpio["servicio"]
            .isin(servicios_validos),
            pd.NA
        )
    )


    # convertir columnas numéricas
    data_frame_limpio["id"] = pd.to_numeric(
        data_frame_limpio["id"],
        errors="coerce"
    )


    data_frame_limpio["costo"] = pd.to_numeric(
        data_frame_limpio["costo"],
        errors="coerce"
    )


    # convertir a fecha
    data_frame_limpio["fecha"] = pd.to_datetime(
        data_frame_limpio["fecha"],
        errors="coerce"
    )


    # reemplazar fechas nulas
    fecha_defecto = pd.to_datetime("2026-01-01")


    data_frame_limpio["fecha"] = (
        data_frame_limpio["fecha"]
        .fillna(fecha_defecto)
    )


    # eliminar filas con datos obligatorios vacíos
    columnas_obligatorias = [
        "id",
        "servicio",
        "costo",
        "codigo"
    ]


    data_frame_limpio = data_frame_limpio.dropna(
        subset=columnas_obligatorias
    )


    # eliminar valores inválidos
    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["costo"] >= 100000
    ]


    data_frame_limpio = data_frame_limpio[
        data_frame_limpio["id"] > 0
    ]


    # eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()


    return data_frame_limpio

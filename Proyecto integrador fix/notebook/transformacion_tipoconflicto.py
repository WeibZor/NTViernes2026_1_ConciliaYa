import pandas as pd

def transformar_datos_tipoConflicto(data_frame_limpio):

    # transformacion 1 (descripciones de reclamos de pago)
    filtro1 = data_frame_limpio.query("Nombre == 'pago'")
    agrupacion1 = filtro1.groupby("Descripcion")["Id"].count().reset_index(name="conteo")

    # transformacion 2 (estado de actividad en contratos)
    filtro2 = data_frame_limpio.query("Nombre == 'contrato'")
    agrupacion2 = filtro2.groupby("Activo")["Id"].count().reset_index(name="conteo")

    # transformacion 3 (nombres vs descripción para mapa de calor activo)
    filtro3 = data_frame_limpio.query("Activo == True")
    agrupacion3 = filtro3.groupby(["Nombre", "Descripcion"])["Id"].count().reset_index(name="conteo")

    # transformacion 4 (variedad de descripciones inactivas)
    filtro4 = data_frame_limpio.query("Activo == False")
    agrupacion4 = filtro4.groupby("Descripcion")["Id"].count().reset_index(name="conteo")

    # transformacion 5 (servicios activos por id)
    filtro5 = data_frame_limpio.query("Nombre == 'servicio' and Activo == True")
    agrupacion5 = filtro5.groupby("Id")["Id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
import pandas as pd

def transformar_datos_estadoConflictos(data_frame_limpio):

    # transformacion 1 (códigos asignados al nombre abierto)
    filtro1 = data_frame_limpio.query("nombre == 'abierto'")
    agrupacion1 = filtro1.groupby("codigo")["id"].count().reset_index(name="conteo")

    # transformacion 2 (descripciones aplicadas al código de cierre)
    filtro2 = data_frame_limpio.query("codigo == 'CER002'")
    agrupacion2 = filtro2.groupby("descripcion")["id"].count().reset_index(name="conteo")

    # transformacion 3 (nombre vs código para mapa de calor activo)
    filtro3 = data_frame_limpio.query("estado == True")
    agrupacion3 = filtro3.groupby(["nombre", "codigo"])["id"].count().reset_index(name="conteo")

    # transformacion 4 (descripciones en estados en proceso)
    filtro4 = data_frame_limpio.query("nombre == 'proceso'")
    agrupacion4 = filtro4.groupby("descripcion")["id"].count().reset_index(name="conteo")

    # transformacion 5 (conteo de ids de estados inactivos con rango bajo)
    filtro5 = data_frame_limpio.query("estado == False and id < 50")
    agrupacion5 = filtro5.groupby("id")["id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
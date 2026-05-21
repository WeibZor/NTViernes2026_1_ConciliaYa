import pandas as pd

def transformar_datos_perfil(data_frame_limpio):

    # transformacion 1 (descripciones aplicadas al administrador)
    filtro1 = data_frame_limpio.query("nombre == 'administrador'")
    agrupacion1 = filtro1.groupby("descripcion")["id"].count().reset_index(name="conteo")

    # transformacion 2 (línea de tiempo de creación de perfiles activos)
    filtro2 = data_frame_limpio.query("activo == True")
    agrupacion2 = filtro2.groupby("fecha")["id"].count().reset_index(name="conteo")

    # transformacion 3 (nombre vs descripción para mapa de calor con IDs altas)
    filtro3 = data_frame_limpio.query("id > 50")
    agrupacion3 = filtro3.groupby(["nombre", "descripcion"])["id"].count().reset_index(name="conteo")

    # transformacion 4 (estado de actividad en roles de usuario)
    filtro4 = data_frame_limpio.query("nombre == 'usuario'")
    agrupacion4 = filtro4.groupby("activo")["id"].count().reset_index(name="conteo")

    # transformacion 5 (descripciones de gestores inactivos)
    filtro5 = data_frame_limpio.query("nombre == 'gestor' and activo == False")
    agrupacion5 = filtro5.groupby("descripcion")["id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
import pandas as pd

def transformar_datos_usuarios(data_frame_limpio):

    # transformacion 1 (usuarios activos por fecha de alta)
    filtro1 = data_frame_limpio.query("Activo == True")
    agrupacion1 = filtro1.groupby("FechaAlta")["Id"].count().reset_index(name="conteo")

    # transformacion 2 (perfiles asignados a usuarios con DNI)
    filtro2 = data_frame_limpio.query("TipoDocumento == 'DNI'")
    agrupacion2 = filtro2.groupby("PerfilId")["Id"].count().reset_index(name="conteo")

    # transformacion 3 (documentos por administrador para mapa de calor)
    filtro3 = data_frame_limpio.query("UsuarioAltaId == 1")
    agrupacion3 = filtro3.groupby(["TipoDocumento", "Apellido"])["Id"].count().reset_index(name="conteo")

    # transformacion 4 (estado de actividad en un perfil específico)
    filtro4 = data_frame_limpio.query("PerfilId == 3")
    agrupacion4 = filtro4.groupby("Activo")["Id"].count().reset_index(name="conteo")

    # transformacion 5 (apellidos de pasaportes inactivos)
    filtro5 = data_frame_limpio.query("Activo == False and TipoDocumento == 'PASAPORTE'")
    agrupacion5 = filtro5.groupby("Apellido")["Id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
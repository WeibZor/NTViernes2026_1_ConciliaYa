import pandas as pd

def transformar_datos_conflicto(data_frame_limpio):

    # transformacion 1 (demandas millonarias por fecha de inicio)
    filtro1 = data_frame_limpio.query("MontoReclamado > 50000")
    agrupacion1 = filtro1.groupby("FechaInicio")["Id"].count().reset_index(name="conteo")

    # transformacion 2 (resultados de los casos cerrados)
    filtro2 = data_frame_limpio.query("FechaCierre.notna()")
    agrupacion2 = filtro2.groupby("Resultado")["Id"].count().reset_index(name="conteo")

    # transformacion 3 (tipo vs estado para mapa de calor activo)
    filtro3 = data_frame_limpio.query("Activo == True")
    agrupacion3 = filtro3.groupby(["TipoConflictoId", "EstadoConflictoId"])["Id"].count().reset_index(name="conteo")

    # transformacion 4 (estados del conflicto en reclamos de pago tipo 1)
    filtro4 = data_frame_limpio.query("TipoConflictoId == 1")
    agrupacion4 = filtro4.groupby("EstadoConflictoId")["Id"].count().reset_index(name="conteo")

    # transformacion 5 (asuntos recurrentes de los primeros demandantes)
    filtro5 = data_frame_limpio.query("UsuarioDemandanteId <= 20")
    agrupacion5 = filtro5.groupby("Asunto")["Id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
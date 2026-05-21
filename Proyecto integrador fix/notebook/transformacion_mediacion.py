import pandas as pd

def transformar_datos_mediacion(data_frame_limpio):

    # transformacion 1 (acuerdos firmados por fecha programada)
    filtro1 = data_frame_limpio.query("Resultado == 'Acuerdo firmado'")
    agrupacion1 = filtro1.groupby("FechaProgramada")["Id"].count().reset_index(name="conteo")

    # transformacion 2 (resultados de audiencias presenciales)
    filtro2 = data_frame_limpio.query("Lugar == 'Oficina Av. Corrientes 1234'")
    agrupacion2 = filtro2.groupby("Resultado")["Id"].count().reset_index(name="conteo")

    # transformacion 3 (mediador vs lugar para mapa de calor de activos)
    filtro3 = data_frame_limpio.query("UsuarioMediadorId <= 5 and Activo == True")
    agrupacion3 = filtro3.groupby(["UsuarioMediadorId", "Lugar"])["Id"].count().reset_index(name="conteo")

    # transformacion 4 (lugares elegidos para mediaciones que siguen en curso)
    filtro4 = data_frame_limpio.query("Resultado == 'Mediación en curso'")
    agrupacion4 = filtro4.groupby("Lugar")["Id"].count().reset_index(name="conteo")

    # transformacion 5 (observaciones de casos con estado no definido)
    filtro5 = data_frame_limpio.query("EstadoConflictoId.isna()")
    agrupacion5 = filtro5.groupby("Observaciones")["Id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen
import pandas as pd
import random
from datetime import datetime, timedelta


def generar_simulacion_mediacion(numeroSimulaciones):
    lugares = ["Oficina Av. Corrientes 1234", "Sala Virtual Zoom 3", "Oficina Central Piso 4"]
    observaciones = ["Las partes aportaron pruebas.", "Se solicita cuarto intermedio.", "Abogados presentes."]
    resultados = ["Mediación en curso", "Acuerdo firmado", "Fracasó por ausencia"]
    
    mediaciones = []
    fechaRegistroBase = datetime(2026, 3, 25)

    for _ in range(numeroSimulaciones):
        mediacion = {
            "Id": rd.randint(300, 999),
            "ConflictoId": rd.randint(100, 999),
            "UsuarioMediadorId": rd.randint(1, 50),
            "EstadoConflictoId": rd.choice([1, 2, 3, None]),
            "FechaProgramada": fechaRegistroBase + timedelta(days=rd.randint(1, 10)),
            "Lugar": rd.choice(lugares),
            "Observaciones": rd.choice(observaciones),
            "Resultado": rd.choice(resultados),
            "FechaRegistro": fechaRegistroBase,
            "Activo": rd.choice([True, False])
        }

        # Inyectando errores controlados (Igual al ejemplo base)
        probabilidadError = rd.random()
        if probabilidadError < 0.2:
            mediacion["Id"] = None
        elif probabilidadError < 0.4:
            mediacion["Lugar"] = rd.choice(["LugarFalso1", "LugarFalso2"])
        elif probabilidadError < 0.5:
            mediacion["ConflictoId"] = rd.choice([0, -1, None])
        elif probabilidadError < 0.8:
            mediacion["Observaciones"] = " " + mediacion["Observaciones"].upper()
        elif probabilidadError < 0.9:
            mediacion["FechaProgramada"] = None

        mediaciones.append(mediacion)
    return mediaciones
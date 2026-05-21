import random as rd
from datetime import datetime, timedelta

# ==========================================
# 1. SIMULACIÓN: TABLA CONFLICTO (AISLADA)
# ==========================================
def generar_simulacion_conflicto(numeroSimulaciones):
    asuntos = ["Pago factura atrasada", "Incumplimiento de contrato", "Falla en servicio contratado", "Reclamo de garantía"]
    descripciones = ["El cliente no abonó el saldo.", "No se entregó el software en la fecha.", "Cortes de internet.", "El producto falló."]
    resultados = ["Acuerdo parcial", "Rescisión sin multa", "Compensación", "Cambio de producto"]
    
    conflictos = []
    fechaInicioBase = datetime(2026, 3, 20)

    for _ in range(numeroSimulaciones):
        conflicto = {
            "Id": rd.randint(100, 999),
            "UsuarioDemandanteId": rd.randint(1, 100),
            "UsuarioDemandadoId": rd.randint(1, 100),
            "TipoConflictoId": rd.randint(1, 10),
            "EstadoConflictoId": rd.randint(1, 5),
            "Asunto": rd.choice(asuntos),
            "Descripcion": rd.choice(descripciones),
            "FechaInicio": fechaInicioBase + timedelta(days=rd.randint(0, 30)),
            "FechaCierre": rd.choice([None, fechaInicioBase + timedelta(days=rd.randint(31, 60))]),
            "Resultado": rd.choice(resultados),
            "MontoReclamado": round(rd.uniform(1000.00, 50000.00), 2),
            "Activo": rd.choice([True, False]),
            "FechaAlta": fechaInicioBase + timedelta(minutes=rd.randint(5, 60))
        }

        # Inyectando errores controlados (Igual al ejemplo base)
        probabilidadError = rd.random()
        if probabilidadError < 0.2:
            conflicto["Id"] = None
        elif probabilidadError < 0.4:
            conflicto["Asunto"] = rd.choice(["Asunto_Invalido", "TEST_ERROR"])
        elif probabilidadError < 0.5:
            conflicto["MontoReclamado"] = rd.choice([0, -5000, None])
        elif probabilidadError < 0.8:
            conflicto["Descripcion"] = " " + conflicto["Descripcion"].upper()
        elif probabilidadError < 0.9:
            conflicto["FechaInicio"] = None

        conflictos.append(conflicto)
    return conflictos



import random as rd

def generar_simulacion_tipoConflicto(numeroSimulaciones):
    listaNombres = ["Pago", "Contrato", "Servicio"]
    listaDescripciones = ["Reclamo por pago pendiente", "Incumplimiento de contrato", "Falla en el servicio"]
    
    tiposConflicto = []

    for _ in range(numeroSimulaciones):
        tipoConflicto = {
            "Id": rd.randint(1, 50),
            "Nombre": rd.choice(listaNombres),
            "Descripcion": rd.choice(listaDescripciones),
            "Activo": rd.choice([True, False])
        }

        # Inyectando errores controlados
        probabilidadError = rd.random()
        if probabilidadError < 0.2:
            tipoConflicto["Id"] = None
        elif probabilidadError < 0.4:
            tipoConflicto["Nombre"] = rd.choice(["clase de python", "clase de ingles"])
        elif probabilidadError < 0.5:
            tipoConflicto["Id"] = rd.choice([0, -1000, None])
        elif probabilidadError < 0.8:
            tipoConflicto["Descripcion"] = " " + tipoConflicto["Descripcion"].upper()
        elif probabilidadError < 0.9:
            tipoConflicto["Activo"] = None

        tiposConflicto.append(tipoConflicto)
    return tiposConflicto

# Ejemplo de uso con 5 registros:
# print(generar_simulacion_tipoConflicto(5))
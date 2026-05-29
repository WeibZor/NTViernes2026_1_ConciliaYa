import random as rd

# Simula la respuesta de GET /api/tipos-conflicto
# DTO: { id, nombre, descripcion, activo }

def generar_simulacion_tipoConflicto(num):
    nombres  = ["Pago", "Contrato", "Servicio"]
    descrips = [
        "Reclamo por pago pendiente o factura vencida",
        "Incumplimiento de cláusulas contractuales",
        "Falla o interrupción en el servicio contratado"
    ]

    resultado = []
    for _ in range(num):
        idx = rd.randint(0, 2)
        registro = {
            "id":          rd.randint(1, 50),
            "nombre":      nombres[idx],
            "descripcion": descrips[idx],
            "activo":      rd.choice([True, False])
        }

        # Errores controlados
        p = rd.random()
        if p < 0.15:
            registro["id"] = None
        elif p < 0.30:
            registro["nombre"] = rd.choice(["clase de python", "INVALIDO", None])
        elif p < 0.50:
            registro["activo"] = None
        elif p < 0.75:
            registro["descripcion"] = "  " + registro["descripcion"].upper()

        resultado.append(registro)
    return resultado

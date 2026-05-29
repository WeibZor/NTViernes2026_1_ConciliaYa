import random as rd

# Simula la respuesta de GET /api/estados-conflicto
# DTO: { id, nombre, codigo, descripcion, activo }

def generar_estadoConflictos(num):
    nombres   = ["Abierto", "Cerrado", "En Proceso"]
    codigos   = ["ABR001",  "CER002",  "PRO003"]
    descrips  = [
        "Conflicto abierto pendiente de resolución",
        "Conflicto cerrado y finalizado",
        "Conflicto en proceso de mediación"
    ]

    resultado = []
    for _ in range(num):
        idx = rd.randint(0, 2)
        registro = {
            "id":          rd.randint(1, 100),
            "nombre":      nombres[idx],
            "codigo":      codigos[idx],
            "descripcion": descrips[idx],
            "activo":      rd.choice([True, False])
        }

        # Errores controlados
        p = rd.random()
        if p < 0.15:
            registro["id"] = None
        elif p < 0.30:
            registro["nombre"] = rd.choice(["INVALIDO", "TEST_ERROR", None])
        elif p < 0.45:
            registro["codigo"] = "  " + registro["codigo"] + "  "   # espacios sucios
        elif p < 0.70:
            registro["descripcion"] = "  " + registro["descripcion"].upper()

        resultado.append(registro)
    return resultado

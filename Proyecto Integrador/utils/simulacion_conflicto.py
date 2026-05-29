import random as rd
from datetime import datetime, timedelta

# Simula la respuesta de GET /api/conflictos
# El controller devuelve la entidad Conflicto completa con objetos anidados:
# usuarioDemandante{...}, usuarioDemandado{...}, tipoConflicto{...}, estadoConflicto{...}
# Campos planos: id, asunto, descripcion, fechaInicio, fechaCierre,
#                resultado, montoReclamado, activo, fechaAlta

TIPOS = [
    {"id": 1, "nombre": "Pago",      "descripcion": "Reclamo por pago pendiente",             "activo": True},
    {"id": 2, "nombre": "Contrato",  "descripcion": "Incumplimiento de cláusulas contractuales","activo": True},
    {"id": 3, "nombre": "Servicio",  "descripcion": "Falla en el servicio contratado",         "activo": True},
]

ESTADOS = [
    {"id": 1, "nombre": "Abierto",     "codigo": "ABR001", "descripcion": "Conflicto abierto pendiente", "activo": True},
    {"id": 2, "nombre": "Cerrado",     "codigo": "CER002", "descripcion": "Conflicto cerrado",            "activo": True},
    {"id": 3, "nombre": "En Proceso",  "codigo": "PRO003", "descripcion": "En proceso de mediación",      "activo": True},
]

USUARIOS_BASE = [
    {"id": i, "nombre": n, "apellido": a, "correo": f"{n.lower()}@empresa.com",
     "tipoDocumento": "DNI", "documento": str(10000000+i*3), "telefono": "+57 300 0000000",
     "perfil": {"id": 2, "nombre": "gestor", "descripcion": "Acceso limitado", "activo": True},
     "activo": True, "fechaAlta": "2026-01-15T09:00:00"}
    for i, (n, a) in enumerate([
        ("María","González"),("Juan","Rodríguez"),("Carlos","Pérez"),
        ("Ana","Gómez"),("Luis","López"),("Sofía","Martínez")
    ], start=1)
]

def generar_simulacion_conflicto(num):
    asuntos    = ["Pago de factura vencida", "Incumplimiento de contrato", "Falla en servicio", "Reclamo de garantía"]
    resultados = ["Acuerdo parcial", "Rescisión sin multa", "Compensación acordada", "Cambio de producto", None]
    fecha_base = datetime(2026, 1, 1)

    resultado = []
    for _ in range(num):
        fi = fecha_base + timedelta(days=rd.randint(0, 100))
        fc = fi + timedelta(days=rd.randint(10, 60)) if rd.random() > 0.4 else None

        registro = {
            "id":                  rd.randint(1, 1000),
            "usuarioDemandante":   rd.choice(USUARIOS_BASE),
            "usuarioDemandado":    rd.choice(USUARIOS_BASE),
            "tipoConflicto":       rd.choice(TIPOS),
            "estadoConflicto":     rd.choice(ESTADOS),
            "asunto":              rd.choice(asuntos),
            "descripcion":         "Descripción del caso registrado.",
            "fechaInicio":         fi.strftime("%Y-%m-%dT%H:%M:%S"),
            "fechaCierre":         fc.strftime("%Y-%m-%dT%H:%M:%S") if fc else None,
            "resultado":           rd.choice(resultados),
            "montoReclamado":      round(rd.uniform(500.0, 80000.0), 2),
            "activo":              rd.choice([True, False]),
            "fechaAlta":           fi.strftime("%Y-%m-%dT%H:%M:%S")
        }

        # Errores controlados
        p = rd.random()
        if p < 0.15:
            registro["id"] = None
        elif p < 0.30:
            registro["asunto"] = rd.choice(["ASUNTO_INVALIDO", "TEST_ERROR", None])
        elif p < 0.45:
            registro["montoReclamado"] = rd.choice([0, -999, None])
        elif p < 0.60:
            registro["tipoConflicto"] = None      # FK rota
        elif p < 0.80:
            registro["descripcion"] = "  " + registro["descripcion"].upper()

        resultado.append(registro)
    return resultado

import random as rd
from datetime import datetime, timedelta

# Simula la respuesta de GET /api/mediaciones
# Entidad completa con objetos anidados:
# conflicto{...}, usuarioMediador{...}, estadoConflicto{...}
# Campos planos: id, fechaProgramada, lugar, observaciones, resultado, fechaRegistro, activo

ESTADOS = [
    {"id": 1, "nombre": "Abierto",    "codigo": "ABR001", "descripcion": "Conflicto abierto",          "activo": True},
    {"id": 2, "nombre": "Cerrado",    "codigo": "CER002", "descripcion": "Conflicto cerrado",           "activo": True},
    {"id": 3, "nombre": "En Proceso", "codigo": "PRO003", "descripcion": "En proceso de mediación",     "activo": True},
]

MEDIADORES = [
    {"id": i, "nombre": n, "apellido": a, "correo": f"{n.lower()}@empresa.com",
     "tipoDocumento": "DNI", "documento": str(20000000+i*7), "telefono": "+57 310 0000000",
     "perfil": {"id": 1, "nombre": "administrador", "descripcion": "Acceso total", "activo": True},
     "activo": True, "fechaAlta": "2026-01-10T08:00:00"}
    for i, (n, a) in enumerate([
        ("Elena","Torres"),("Ricardo","Vega"),("Patricia","Ruiz"),("Fernando","Castro")
    ], start=10)
]

# Conflictos de referencia simplificados (sin anidar usuarios completos)
CONFLICTOS_REF = [{"id": i, "asunto": f"Caso #{i}", "activo": True} for i in range(100, 150)]

def generar_simulacion_mediacion(num):
    lugares = [
        "Oficina Central Piso 2",
        "Sala Virtual Zoom",
        "Sede Norte Sala A",
        "Sede Sur Sala B"
    ]
    observaciones = [
        "Las partes presentaron pruebas documentales.",
        "Se solicitó cuarto intermedio para deliberar.",
        "Abogados de ambas partes presentes.",
        "Mediación express acordada por ambas partes."
    ]
    resultados = ["Acuerdo firmado", "Mediación en curso", "Fracasó por ausencia", "Derivado a instancia judicial"]
    fecha_base = datetime(2026, 2, 1)

    resultado = []
    for _ in range(num):
        fp = fecha_base + timedelta(days=rd.randint(0, 120))
        fr = fp - timedelta(days=rd.randint(1, 5))

        registro = {
            "id":               rd.randint(1, 500),
            "conflicto":        rd.choice(CONFLICTOS_REF),
            "usuarioMediador":  rd.choice(MEDIADORES),
            "estadoConflicto":  rd.choice(ESTADOS),
            "fechaProgramada":  fp.strftime("%Y-%m-%dT%H:%M:%S"),
            "lugar":            rd.choice(lugares),
            "observaciones":    rd.choice(observaciones),
            "resultado":        rd.choice(resultados),
            "fechaRegistro":    fr.strftime("%Y-%m-%dT%H:%M:%S"),
            "activo":           rd.choice([True, False])
        }

        # Errores controlados
        p = rd.random()
        if p < 0.15:
            registro["id"] = None
        elif p < 0.30:
            registro["lugar"] = rd.choice(["LugarFalso", "INVALIDO", None])
        elif p < 0.45:
            registro["conflicto"] = None          # FK rota
        elif p < 0.60:
            registro["resultado"] = None
        elif p < 0.80:
            registro["observaciones"] = "  " + registro["observaciones"].upper()

        resultado.append(registro)
    return resultado

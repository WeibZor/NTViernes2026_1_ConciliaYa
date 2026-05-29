import random as rd
from datetime import datetime, timedelta

# Simula la respuesta de GET /api/usuarios
# El controller devuelve la entidad Usuario completa (no el DTO),
# por lo tanto incluye el objeto "perfil" anidado y fechaAlta.
# Campos: { id, nombre, apellido, tipoDocumento, documento, correo,
#            telefono, perfil:{id,nombre,descripcion,activo}, activo, fechaAlta }

PERFILES = [
    {"id": 1, "nombre": "administrador", "descripcion": "Acceso total al sistema",                     "activo": True},
    {"id": 2, "nombre": "gestor",        "descripcion": "Acceso limitado a gestión de conflictos",     "activo": True},
    {"id": 3, "nombre": "usuario",       "descripcion": "Acceso restringido a consulta",               "activo": True},
]

def generar_simulacion_usuarios(num):
    nombres   = ["María", "Juan", "Carlos", "Ana", "Luis", "Sofía", "Pedro", "Laura"]
    apellidos = ["González", "Rodríguez", "Pérez", "Gómez", "López", "Martínez"]
    tipos_doc = ["DNI", "CUIT", "Pasaporte"]
    fecha_base = datetime(2026, 1, 1)

    resultado = []
    for _ in range(num):
        nombre   = rd.choice(nombres)
        apellido = rd.choice(apellidos)
        tipo_doc = rd.choice(tipos_doc)
        perfil   = rd.choice(PERFILES)
        fecha    = fecha_base + timedelta(days=rd.randint(0, 148))

        registro = {
            "id":            rd.randint(1, 500),
            "nombre":        nombre,
            "apellido":      apellido,
            "tipoDocumento": tipo_doc,
            "documento":     str(rd.randint(10000000, 45000000)),
            "correo":        f"{nombre.lower()}.{apellido.lower()}@empresa.com",
            "telefono":      f"+57 300 {rd.randint(1000000, 9999999)}",
            "perfil":        perfil,
            "activo":        rd.choice([True, False]),
            "fechaAlta":     fecha.strftime("%Y-%m-%dT%H:%M:%S")
        }

        # Errores controlados
        p = rd.random()
        if p < 0.15:
            registro["id"] = None
        elif p < 0.30:
            registro["nombre"] = rd.choice(["INVALIDO", "clase de python", None])
        elif p < 0.45:
            registro["perfil"] = None           # FK rota
        elif p < 0.60:
            registro["correo"] = "correo_sin_arroba"   # formato inválido
        elif p < 0.80:
            registro["tipoDocumento"] = "  " + registro["tipoDocumento"] + "  "

        resultado.append(registro)
    return resultado

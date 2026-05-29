import random as rd

# Simula la respuesta de GET /api/perfiles
# DTO: { id, nombre, descripcion, activo }
# IMPORTANTE: el PerfilDto NO expone fechaAlta, solo el modelo la tiene internamente.

def generarPerfil(num):
    nombres = ["administrador", "gestor", "usuario"]
    descrips = [
        "Acceso total al sistema",
        "Acceso limitado a gestión de conflictos",
        "Acceso restringido a consulta"
    ]

    resultado = []
    for _ in range(num):
        idx = rd.randint(0, 2)
        registro = {
            "id":          rd.randint(1, 10),
            "nombre":      nombres[idx],
            "descripcion": descrips[idx],
            "activo":      rd.choice([True, False])
        }

        # Errores controlados
        p = rd.random()
        if p < 0.15:
            registro["id"] = None
        elif p < 0.30:
            registro["nombre"] = rd.choice(["INVALIDO", "sin_nombre", None])
        elif p < 0.50:
            registro["descripcion"] = None
        elif p < 0.75:
            registro["descripcion"] = "  " + registro["descripcion"].upper()

        resultado.append(registro)
    return resultado

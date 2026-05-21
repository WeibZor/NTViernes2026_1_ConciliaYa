import random as rd
from datetime import datetime, timedelta

def generar_simulacion_usuarios(numeroSimulaciones):
    listaNombres = ["María", "Juan", "Carlos", "Ana", "Luis", "Sofía"]
    listaApellidos = ["González", "Rodríguez", "Pérez", "Gómez", "López", "Martínez"]
    listaTiposDoc = ["DNI", "CUIT", "Pasaporte"]
    
    usuarios = []
    fechaAltaBase = datetime(2026, 1, 15, 9, 30, 0)

    for _ in range(numeroSimulaciones):
        nombre = rd.choice(listaNombres)
        apellido = rd.choice(listaApellidos)
        
        usuario = {
            "Id": rd.randint(1, 200),
            "Nombre": nombre,
            "Apellido": apellido,
            "TipoDocumento": rd.choice(listaTiposDoc),
            "Documento": str(rd.randint(10000000, 45000000)),
            "Correo": f"{nombre.lower()}@gmail.com",
            "Telefono": f"+54 9 11 {rd.randint(1000, 9999)} {rd.randint(1000, 9999)}",
            "PerfilId": rd.randint(1, 5),
            "Activo": rd.choice([True, False]),
            "FechaAlta": fechaAltaBase + timedelta(days=rd.randint(0, 10)),
            "UsuarioAltaId": rd.choice([1, 2, 3, None])
        }

        # Inyectando errores controlados
        probabilidadError = rd.random()
        if probabilidadError < 0.2:
            usuario["Id"] = None
        elif probabilidadError < 0.4:
            usuario["Nombre"] = rd.choice(["clase de python", "clase de ingles"])
        elif probabilidadError < 0.5:
            usuario["PerfilId"] = rd.choice([0, -1000, None])
        elif probabilidadError < 0.8:
            usuario["TipoDocumento"] = " " + usuario["TipoDocumento"].upper()
        elif probabilidadError < 0.9:
            usuario["FechaAlta"] = None

        usuarios.append(usuario)
    return usuarios

# Ejemplo de uso con 5 registros para probar:
# print(generar_simulacion_usuarios(5))
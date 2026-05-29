import requests

def consumir_usuario():
    url = "http://localhost:8080/api/usuarios"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

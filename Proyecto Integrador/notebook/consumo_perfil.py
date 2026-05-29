import requests

def consumir_perfil():
    url = "http://localhost:8080/api/perfiles"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

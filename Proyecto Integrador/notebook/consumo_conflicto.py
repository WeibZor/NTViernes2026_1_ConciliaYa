import requests

def consumir_conflicto():
    url = "http://localhost:8080/api/conflictos"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

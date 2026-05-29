import requests

def consumir_mediacion():
    url = "http://localhost:8080/api/mediaciones"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

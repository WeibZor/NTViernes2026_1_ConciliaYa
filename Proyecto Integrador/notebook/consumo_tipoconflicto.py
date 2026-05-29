import requests

def consumir_tipo_conflicto():
    url = "http://localhost:8080/api/tipos-conflicto"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

import requests

def consumir_estadoconflicto():
    url = "http://localhost:8080/api/estados-conflicto"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

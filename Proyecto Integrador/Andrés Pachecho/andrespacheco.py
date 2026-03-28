# Simulación de datos - Tabla Mediacion

import random
import json
import csv
from datetime import datetime, timedelta


# Simulación de datos - Tabla Mediacion

import random
import json
import csv
from datetime import datetime, timedelta


def generar_mediaciones(numeroRegistros):

    tiposMediacion = ["Familiar", "Laboral", "Civil", "Penal"]
    estados = ["Pendiente", "En proceso", "Finalizado", "Cancelado"]

    fechaInicio = datetime(2026, 1, 1)

    mediaciones = []

    for i in range(numeroRegistros):

        fecha = fechaInicio + timedelta(days=random.randint(0, 60))

        mediacion = {
            "id": i + 1,
            "tipo": random.choice(tiposMediacion),
            "estado": random.choice(estados),
            "id_cliente": random.randint(1, 200),
            "id_mediador": random.randint(1, 50),
            "costo": random.randint(100000, 1000000),
            "fecha": fecha.strftime("%Y-%m-%d")
        }

        mediaciones.append(mediacion)

    return mediaciones


# -------- GUARDAR JSON --------
def guardar_json(datos, nombreArchivo):
    with open(nombreArchivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


# -------- GUARDAR CSV --------
def guardar_csv(datos, nombreArchivo):

    if len(datos) == 0:
        return

    claves = datos[0].keys()

    with open(nombreArchivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=claves)
        writer.writeheader()
        writer.writerows(datos)


# -------- CARGAR JSON --------
def cargar_json(nombreArchivo):
    with open(nombreArchivo, "r", encoding="utf-8") as f:
        return json.load(f)


# -------- PROGRAMA PRINCIPAL --------
if __name__ == "__main__":

    # Generar 1000 registros
    datos = generar_mediaciones(1000)

    # Exportar archivos
    guardar_json(datos, "mediaciones.json")
    guardar_csv(datos, "mediaciones.csv")

    # Recargar datos
    datos_recargados = cargar_json("mediaciones.json")

    # Validación
    print("Registros generados:", len(datos))
    print("Registros recargados:", len(datos_recargados))
import pandas as pd
import random
from datetime import datetime, timedelta


def generar_mediaciones(numero_registros=1000):
    """Genera un dataset de mediación con al menos 1000 registros."""
    tipos = ["Familiar", "Laboral", "Civil", "Penal"]
    estados = ["Pendiente", "En proceso", "Finalizado", "Cancelado"]
    lugares = ["Sala A", "Sala B", "Sala C", "Sala D"]
    resultados = ["Acuerdo", "Sin acuerdo", "Retrasado", "Cancelado"]

    fecha_inicio = datetime(2026, 1, 1)
    filas = []

    for i in range(numero_registros):
        fecha_programada = fecha_inicio + timedelta(days=random.randint(0, 120))
        fecha_registro = fecha_programada - timedelta(days=random.randint(0, 15))
        filas.append(
            {
                "id": i + 1,
                "conflicto_id": random.randint(1, 400),
                "usuario_mediador_id": random.randint(1, 40),
                "estado_conflicto_id": random.randint(1, 5),
                "tipo": random.choice(tipos),
                "estado": random.choice(estados),
                "fecha_programada": fecha_programada.strftime("%Y-%m-%d"),
                "lugar": random.choice(lugares),
                "observaciones": "Revisión de caso y seguimiento.",
                "resultado": random.choice(resultados),
                "costo": round(random.uniform(150000, 1500000), 2),
                "fecha_registro": fecha_registro.strftime("%Y-%m-%d"),
                "activo": random.choice([True, False])
            }
        )

    return pd.DataFrame(filas)


def guardar_mediaciones_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False, encoding="utf-8")


def guardar_mediaciones_json(df, nombre_archivo):
    df.to_json(nombre_archivo, orient="records", date_format="iso", force_ascii=False)


def cargar_mediaciones_csv(nombre_archivo):
    return pd.read_csv(nombre_archivo, parse_dates=["fecha_programada", "fecha_registro"])


def cargar_mediaciones_json(nombre_archivo):
    return pd.read_json(nombre_archivo, orient="records", convert_dates=["fecha_programada", "fecha_registro"])


if __name__ == "__main__":
    df = generar_mediaciones(1000)
    guardar_mediaciones_csv(df, "mediaciones_simulacion.csv")
    guardar_mediaciones_json(df, "mediaciones_simulacion.json")

    df_csv = cargar_mediaciones_csv("mediaciones_simulacion.csv")
    df_json = cargar_mediaciones_json("mediaciones_simulacion.json")

    print("Registros generados:", len(df))
    print("Registros CSV:", len(df_csv))
    print("Registros JSON:", len(df_json))
    print("Columnas generadas:", df.columns.tolist())

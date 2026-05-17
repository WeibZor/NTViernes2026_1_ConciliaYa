import pandas as pd
import random
from datetime import datetime, timedelta


def generar_fecha_alta(max_dias_atras=365):
    fecha = datetime.now() - timedelta(
        days=random.randint(0, max_dias_atras),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return fecha.strftime("%Y-%m-%d %H:%M:%S")


def generar_datos_conflicto(num_registros=1000, semilla=None):
    """Genera un DataFrame sintético para la tabla Conflicto."""
    if num_registros < 1:
        raise ValueError("num_registros debe ser >= 1")

    if semilla is not None:
        random.seed(semilla)

    tipos = ["Laboral", "Familiar", "Comercial", "Penal", "Civil", "Administrativo", "Consumidor", "Ambiental"]
    estados = ["Abierto", "Cerrado", "En Proceso", "Archivado"]
    descripciones = [
        "Disputa entre partes de carácter laboral.",
        "Problema familiar en curso.",
        "Conflicto comercial derivado de un servicio.",
        "Caso penal con investigaciones activas.",
        "Litigio civil en trámite.",
        "Reclamo administrativo ante entidad pública.",
        "Queja de consumidor contra proveedor.",
        "Conflicto ambiental por impacto ecológico.",
    ]

    filas = []
    for i in range(1, num_registros + 1):
        tipo = random.choice(tipos)
        estado = random.choice(estados)
        descripcion = random.choice(descripciones)
        fecha_alta = generar_fecha_alta()
        usuario_id = random.choice(range(1, num_registros + 1)) if i > 1 else None
        if usuario_id == i:
            usuario_id = random.randint(1, i - 1) if i - 1 > 0 else None

        fila = {
            "Id": i,
            "Titulo": f"Conflicto {tipo} {i}",
            "Descripcion": descripcion,
            "Tipo Conflicto": tipo,
            "Estado": estado,
            "Activo": random.choice([True, False]),
            "FechaAlta": fecha_alta,
            "UsuarioId": usuario_id,
            "Monto": round(random.uniform(1000, 100000), 2),
        }
        filas.append(fila)

    return pd.DataFrame(filas)


def exportar_datos_conflicto(df, csv_path="conflicto_sintetico.csv", json_path="conflicto_sintetico.json"):
    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=4, force_ascii=False)
    print(f"Exportado: {csv_path} y {json_path}")


def cargar_datos_conflicto(csv_path="conflicto_sintetico.csv", json_path="conflicto_sintetico.json"):
    df_csv = pd.read_csv(csv_path)
    df_json = pd.read_json(json_path)
    return df_csv, df_json


def validar_recarga_conflicto(df_origen, df_csv, df_json):
    assert list(df_origen.columns) == list(df_csv.columns) == list(df_json.columns), "Columnas no coinciden"
    assert len(df_origen) == len(df_csv) == len(df_json), "Cantidad de filas no coincide"

    claves = ["Id", "Titulo", "Tipo Conflicto", "Activo"]
    for col in claves:
        assert df_origen[col].head(5).tolist() == df_csv[col].head(5).tolist(), f"Diferencia en columna {col} entre original y CSV"
        assert df_origen[col].head(5).tolist() == df_json[col].head(5).tolist(), f"Diferencia en columna {col} entre original y JSON"

    print("Recarga validada: estructura y primeros registros coinciden.")


def main():
    df = generar_datos_conflicto(num_registros=1000, semilla=42)
    exportar_datos_conflicto(df)
    df_csv, df_json = cargar_datos_conflicto()
    validar_recarga_conflicto(df, df_csv, df_json)


if __name__ == "__main__":
    main()

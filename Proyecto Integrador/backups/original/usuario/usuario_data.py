import pandas as pd
import random
from datetime import datetime, timedelta


def generar_documento(tipo_documento):
    if tipo_documento == "DNI":
        return str(random.randint(10000000, 49999999))
    elif tipo_documento == "CUIT":
        return f"{random.choice([20, 23, 27, 30])}-{random.randint(10000000, 99999999)}-{random.randint(1, 9)}"
    elif tipo_documento == "CE":
        return f"CE{random.randint(1000000, 9999999)}"
    return str(random.randint(100000000, 999999999))


def generar_telefono():
    return f"+54 9 11 {random.randint(1000, 9999)} {random.randint(1000, 9999)}"


def generar_fecha_alta(max_dias_atras=365):
    fecha = datetime.now() - timedelta(
        days=random.randint(0, max_dias_atras),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return fecha.strftime("%Y-%m-%d %H:%M:%S")


def generar_datos_usuario(num_registros=1000, semilla=None):
    """Genera un DataFrame sintético para la tabla Usuario."""
    if num_registros < 1:
        raise ValueError("num_registros debe ser >= 1")

    if semilla is not None:
        random.seed(semilla)

    nombres = ["María", "José", "Lucía", "Juan", "Camila", "Santiago", "Valentina", "Mateo"]
    apellidos = ["González", "Rodríguez", "Pérez", "López", "Martínez", "Gómez", "Díaz", "Fernández"]
    tipos_documento = ["DNI", "CUIT", "CE", "RUC"]
    perfiles_id = [1, 2, 3]

    filas = []
    for i in range(1, num_registros + 1):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        tipo_doc = random.choice(tipos_documento)
        documento = generar_documento(tipo_doc)
        correo = f"{nombre.lower()}.{apellido.lower()}{i}@ejemplo.com"
        fecha_alta = generar_fecha_alta()
        usuario_alta_id = random.choice(range(1, num_registros + 1)) if i > 1 else None
        if usuario_alta_id == i:
            usuario_alta_id = random.randint(1, i - 1) if i - 1 > 0 else None

        fila = {
            "Id": i,
            "Nombre": nombre,
            "Apellido": apellido,
            "TipoDocumento": tipo_doc,
            "Documento": documento,
            "Correo": correo,
            "Telefono": generar_telefono(),
            "PerfilId": random.choice(perfiles_id),
            "Activo": random.choice([True, False]),
            "FechaAlta": fecha_alta,
            "UsuarioAltaId": usuario_alta_id,
        }
        filas.append(fila)

    return pd.DataFrame(filas)


def exportar_datos_usuario(df, csv_path="usuario_sintetico.csv", json_path="usuario_sintetico.json"):
    """Exporta el DataFrame a CSV y JSON conservando la estructura."""
    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=4, force_ascii=False)
    print(f"Exportado: {csv_path} y {json_path}")


def cargar_datos_usuario(csv_path="usuario_sintetico.csv", json_path="usuario_sintetico.json"):
    df_csv = pd.read_csv(csv_path)
    df_json = pd.read_json(json_path)
    return df_csv, df_json


def validar_recarga_usuario(df_origen, df_csv, df_json):
    """Valida que la recarga de CSV y JSON preserve la estructura básica."""
    assert list(df_origen.columns) == list(df_csv.columns) == list(df_json.columns), "Columnas no coinciden"
    assert len(df_origen) == len(df_csv) == len(df_json), "Cantidad de filas no coincide"

    claves = ["Id", "Nombre", "Apellido", "Correo", "PerfilId"]
    for col in claves:
        assert df_origen[col].head(5).tolist() == df_csv[col].head(5).tolist(), f"Diferencia en columna {col} entre original y CSV"
        assert df_origen[col].head(5).tolist() == df_json[col].head(5).tolist(), f"Diferencia en columna {col} entre original y JSON"

    print("Recarga validada: estructura y primeros registros coinciden.")


def main():
    df = generar_datos_usuario(num_registros=1000, semilla=42)
    exportar_datos_usuario(df, csv_path="usuario_sintetico.csv", json_path="usuario_sintetico.json")
    df_csv, df_json = cargar_datos_usuario(csv_path="usuario_sintetico.csv", json_path="usuario_sintetico.json")
    validar_recarga_usuario(df, df_csv, df_json)


if __name__ == "__main__":
    main()

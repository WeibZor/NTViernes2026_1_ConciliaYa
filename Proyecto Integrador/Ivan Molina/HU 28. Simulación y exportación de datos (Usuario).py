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
    else:
        return str(random.randint(100000000, 999999999))


def generar_telefono():
    return f"+54 9 11 {random.randint(1000, 9999)} {random.randint(1000, 9999)}"


def generar_fecha_alta(max_dias_atras=365):
    fecha = datetime.now() - timedelta(days=random.randint(0, max_dias_atras), hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    return fecha


def generar_datos_usuario(num_registros=1000, semilla=None):
    """Genera dataset sintético para tabla Usuarios."""
    if num_registros < 1:
        raise ValueError("num_registros debe ser >= 1")

    if semilla is not None:
        random.seed(semilla)

    nombres = ["María", "José", "Lucía", "Juan", "Camila", "Santiago", "Valentina", "Mateo"]
    apellidos = ["González", "Rodríguez", "Pérez", "López", "Martínez", "Gómez", "Díaz", "Fernández"]
    tipos_documento = ["DNI", "CUIT", "CE", "RUC"]
    perfis_id = [1, 2, 3]  # 1=Admin, 2=Usuario, 3=Supervisor

    registros = []

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

        registro = {
            'Id': i,
            'Nombre': nombre,
            'Apellido': apellido,
            'TipoDocumento': tipo_doc,
            'Documento': documento,
            'Correo': correo,
            'Telefono': generar_telefono(),
            'PerfilId': random.choice(perfis_id),
            'Activo': random.choice([True, False]),
            'FechaAlta': fecha_alta.strftime('%Y-%m-%d %H:%M:%S'),
            'UsuarioAltaId': usuario_alta_id
        }

        registros.append(registro)

    return pd.DataFrame(registros)


def exportar_datos(df, nombre_base='usuario'):
    df.to_csv(f"{nombre_base}.csv", index=False)
    df.to_json(f"{nombre_base}.json", orient='records', indent=4, force_ascii=False)
    print(f"Exportado a {nombre_base}.csv y {nombre_base}.json")


def cargar_datos(nombre_base='usuario'):
    df_csv = pd.read_csv(f"{nombre_base}.csv")
    df_json = pd.read_json(f"{nombre_base}.json")
    return df_csv, df_json


def validar_recarga(df_original, df_csv, df_json):
    assert list(df_original.columns) == list(df_csv.columns) == list(df_json.columns), "Columnas no coinciden"
    assert len(df_original) == len(df_csv) == len(df_json), "Cantidad de filas no coincide"

    # Validación mínima de los datos clave en las primeras filas
    for col in ['Id', 'Nombre', 'Apellido', 'Correo', 'PerfilId']:
        assert df_original[col].head(5).tolist() == df_csv[col].head(5).tolist(), f"Diferencia en columna {col} entre original y CSV"
        assert df_original[col].head(5).tolist() == df_json[col].head(5).tolist(), f"Diferencia en columna {col} entre original y JSON"

    print("Recarga validada: estructura y primeros registros coinciden.")


def main():
    df = generar_datos_usuario(num_registros=1000, semilla=42)
    print(df.head(10))
    exportar_datos(df, nombre_base='usuario')

    df_csv, df_json = cargar_datos(nombre_base='usuario')
    validar_recarga(df, df_csv, df_json)


if __name__ == "__main__":
    main()
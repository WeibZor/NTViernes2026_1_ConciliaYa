from .usuario_data import (
    cargar_datos_usuario,
    exportar_datos_usuario,
    generar_datos_usuario,
    validar_recarga_usuario,
)


def simular_y_exportar_usuarios(num_registros=1000, semilla=42):
    """HU 28: Simula y exporta el dataset Usuario a CSV y JSON."""
    print("\n[HU 28] Simulación y exportación de datos")
    df = generar_datos_usuario(num_registros=num_registros, semilla=semilla)
    exportar_datos_usuario(df, csv_path="usuario_sintetico.csv", json_path="usuario_sintetico.json")
    return df


def recargar_y_validar_usuarios(df_origen, csv_path="usuario_sintetico.csv", json_path="usuario_sintetico.json"):
    df_csv, df_json = cargar_datos_usuario(csv_path=csv_path, json_path=json_path)
    validar_recarga_usuario(df_origen, df_csv, df_json)
    return df_csv, df_json

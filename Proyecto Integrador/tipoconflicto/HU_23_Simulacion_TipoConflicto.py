from tipoconflicto.tipoconflicto_data import (
    cargar_datos_tipoconflicto,
    exportar_datos_tipoconflicto,
    generar_datos_tipoconflicto,
    validar_recarga_tipoconflicto,
)


def simular_y_exportar_tipos_conflicto(num_registros=1000, semilla=42):
    """HU 23: Simula y exporta el dataset TipoConflicto a CSV y JSON."""
    print("\n[HU 23] Simulación y exportación de datos")
    df = generar_datos_tipoconflicto(num_registros=num_registros, semilla=semilla)
    exportar_datos_tipoconflicto(df, csv_path="tipoconflicto_sintetico.csv", json_path="tipoconflicto_sintetico.json")
    return df


def recargar_y_validar_tipos_conflicto(df_origen, csv_path="tipoconflicto_sintetico.csv", json_path="tipoconflicto_sintetico.json"):
    df_csv, df_json = cargar_datos_tipoconflicto(csv_path=csv_path, json_path=json_path)
    validar_recarga_tipoconflicto(df_origen, df_csv, df_json)
    return df_csv, df_json
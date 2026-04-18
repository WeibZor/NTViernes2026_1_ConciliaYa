import pandas as pd
import random
import json
import os

# Función para generar datos simulados para la tabla TipoConflicto
def generar_datos_tipo_conflicto(num_registros=1000):
    """
    Genera un dataset simulado para la tabla TipoConflicto.

    Args:
        num_registros (int): Número de registros a generar. Por defecto 1000.

    Returns:
        pd.DataFrame: DataFrame con los datos generados.
    """
    # Lista de nombres de tipos de conflicto predefinidos para mayor realismo
    nombres_base = [
        "Pago", "Contrato", "Servicio", "Vecinal", "Familiar", "Laboral",
        "Comercial", "Ambiental", "Tránsito", "Salud", "Educación",
        "Propiedad", "Alquiler", "Seguro", "Tecnológico", "Legal"
    ]

    # Descripciones base correspondientes
    descripciones_base = [
        "Reclamo por pago pendiente",
        "Disputa contractual entre partes",
        "Problema con prestación de servicios",
        "Conflicto entre vecinos",
        "Diferencia familiar",
        "Situación laboral conflictiva",
        "Disputa comercial",
        "Problema ambiental",
        "Incidente de tránsito",
        "Conflicto en servicios de salud",
        "Diferencia educativa",
        "Disputa por propiedad",
        "Problema de alquiler",
        "Reclamo de seguro",
        "Conflicto tecnológico",
        "Asunto legal"
    ]

    datos = []

    for i in range(1, num_registros + 1):
        # Seleccionar nombre y descripción base aleatoriamente
        idx = random.randint(0, len(nombres_base) - 1)
        nombre = nombres_base[idx]
        descripcion = descripciones_base[idx]

        # Agregar variación a la descripción para mayor diversidad
        variaciones = [
            " con implicaciones legales",
            " de carácter urgente",
            " que requiere mediación",
            " con múltiples partes involucradas",
            " de larga duración",
            " recientemente reportado"
        ]
        if random.random() < 0.3:  # 30% de probabilidad de variación
            descripcion += random.choice(variaciones)

        # Generar Activo aleatoriamente (0 o 1)
        activo = random.choice([0, 1])

        # Campos adicionales opcionales
        costo = random.randint(1000, 100000)  # Costo aleatorio entre 1000 y 100000
        cliente_id = random.randint(1, 500)  # ClienteId aleatorio entre 1 y 500

        # Crear registro
        registro = {
            'Id': i,
            'Nombre': nombre,
            'Descripcion': descripcion,
            'Activo': activo,
            'Costo': costo,
            'ClienteId': cliente_id
        }

        datos.append(registro)

    # Crear DataFrame
    df = pd.DataFrame(datos)

    return df

# Función para exportar datos a CSV y JSON
def exportar_datos(df, nombre_archivo_base='tipo_conflicto'):
    """
    Exporta el DataFrame a archivos CSV y JSON.

    Args:
        df (pd.DataFrame): DataFrame a exportar.
        nombre_archivo_base (str): Nombre base para los archivos de salida.
    """
    # Exportar a CSV
    csv_path = f"{nombre_archivo_base}.csv"
    df.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"Datos exportados a {csv_path}")

    # Exportar a JSON
    json_path = f"{nombre_archivo_base}.json"
    df.to_json(json_path, orient='records', indent=4, force_ascii=False)
    print(f"Datos exportados a {json_path}")

# Función principal
def main():
    """
    Función principal que ejecuta la simulación y exportación de datos.
    """
    print("Iniciando simulación de datos para TipoConflicto...")

    # Generar datos (mínimo 1000 registros)
    num_registros = 1000
    df_tipo_conflicto = generar_datos_tipo_conflicto(num_registros)

    print(f"Dataset generado con {len(df_tipo_conflicto)} registros.")

    # Mostrar muestra de los primeros registros
    print("\nMuestra de los primeros 10 registros:")
    print(df_tipo_conflicto.head(10))

    # Exportar datos
    exportar_datos(df_tipo_conflicto)

    print("\nSimulación completada exitosamente.")

# Ejecutar el script si se llama directamente
if __name__ == "__main__":
    main()

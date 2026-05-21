import pandas as pd

def describir_estadoConflictos(df_limpio):
    print("*** DESCRIPCION DEL DATASET: ESTADO CONFLICTOS ***")
    print(f"Numero de filas del dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(df_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{df_limpio.dtypes}\n")

    # Estadísticas (Solo id es numérico)
    print("*** ESTADISTICAS ***")
    print(f"{df_limpio[['id']].describe()}\n")

    # Información de conteos valiosos
    print("*** CONTEOS ***")
    print("Conteo por Nombre de Estado:")
    print(f"{df_limpio['nombre'].value_counts()}\n")
    print("Conteo por Código de Estado:")
    print(f"{df_limpio['codigo'].value_counts()}\n")
    print("Conteo por Estado Booleano (true/false):")
    print(f"{df_limpio['estado'].value_counts()}\n")

    # Describiendo las fechas (Esta tabla NO tiene fechas)
    print("*** DESCRIPCION DE FECHAS ***")
    print("Esta tabla no contiene campos de tipo fecha.\n")
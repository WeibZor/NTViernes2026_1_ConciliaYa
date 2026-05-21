import pandas as pd

def describir_tipoConflicto(df_limpio):
    print("*** DESCRIPCION DEL DATASET: TIPO CONFLICTO ***")
    print(f"Numero de filas del dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(df_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{df_limpio.dtypes}\n")

    # Estadísticas (Solo Id es numérico aquí)
    print("*** ESTADISTICAS ***")
    print(f"{df_limpio[['Id']].describe()}\n")

    # Información de conteos valiosos
    print("*** CONTEOS ***")
    print("Conteo por Nombre de Conflicto:")
    print(f"{df_limpio['Nombre'].value_counts()}\n")
    print("Conteo de Tipos Activos vs Inactivos:")
    print(f"{df_limpio['Activo'].value_counts()}\n")

    # Describiendo las fechas (Esta tabla NO tiene fechas)
    print("*** DESCRIPCION DE FECHAS ***")
    print("Esta tabla no contiene campos de tipo fecha.\n")
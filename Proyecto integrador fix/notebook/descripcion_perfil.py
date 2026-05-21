import pandas as pd

def describir_perfil(df_limpio):
    print("*** DESCRIPCION DEL DATASET: PERFIL ***")
    print(f"Numero de filas del dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(df_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{df_limpio.dtypes}\n")

    # Estadísticas (Solo id es numérico)
    print("*** ESTADISTICAS ***")
    print(f"{df_limpio[['id']].describe()}\n")

    # Información de conteos valiosos
    print("*** CONTEOS ***")
    print("Conteo por Nombre de Perfil:")
    print(f"{df_limpio['nombre'].value_counts()}\n")
    print("Conteo de Perfiles Activos vs Inactivos:")
    print(f"{df_limpio['activo'].value_counts()}\n")

    # Describiendo las fechas (Tiene el campo fecha)
    print("*** DESCRIPCION DE FECHAS ***")
    print(f"Fecha de Perfil más antigua: {df_limpio['fecha'].min()}")
    print(f"Fecha de Perfil más reciente: {df_limpio['fecha'].max()}")
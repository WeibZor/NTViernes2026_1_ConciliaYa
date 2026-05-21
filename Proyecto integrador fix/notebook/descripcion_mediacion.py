import pandas as pd

def describir_mediacion(df_limpio):
    print("*** DESCRIPCION DEL DATASET: MEDIACION ***")
    print(f"Numero de filas del dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(df_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{df_limpio.dtypes}\n")

    # Estadísticas (Campos numéricos e IDs)
    print("*** ESTADISTICAS ***")
    print(f"{df_limpio[['Id', 'ConflictoId', 'UsuarioMediadorId']].describe()}\n")

    # Información de conteos valiosos
    print("*** CONTEOS ***")
    print("Conteo por Resultados de Mediación:")
    print(f"{df_limpio['Resultado'].value_counts()}\n")
    print("Conteo por Lugares utilizados:")
    print(f"{df_limpio['Lugar'].value_counts()}\n")

    # Describiendo las fechas (FechaProgramada y FechaRegistro)
    print("*** DESCRIPCION DE FECHAS ***")
    print(f"Fecha Programada más antigua: {df_limpio['FechaProgramada'].min()}")
    print(f"Fecha Programada más reciente: {df_limpio['FechaProgramada'].max()}\n")
    print(f"Fecha Registro más antigua: {df_limpio['FechaRegistro'].min()}")
    print(f"Fecha Registro más reciente: {df_limpio['FechaRegistro'].max()}")
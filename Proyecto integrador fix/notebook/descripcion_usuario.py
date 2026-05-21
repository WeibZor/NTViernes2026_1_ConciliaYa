import pandas as pd

def describir_usuarios(df_limpio):
    print("*** DESCRIPCION DEL DATASET: USUARIOS ***")
    print(f"Numero de filas del dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(df_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{df_limpio.dtypes}\n")

    # Estadísticas (Campos numéricos)
    print("*** ESTADISTICAS ***")
    # PerfilId y UsuarioAltaId son numéricos de interés además del Id
    print(f"{df_limpio[['Id', 'PerfilId', 'UsuarioAltaId']].describe()}\n")

    # Información de conteos valiosos
    print("*** CONTEOS ***")
    print("Conteo por Tipo de Documento:")
    print(f"{df_limpio['TipoDocumento'].value_counts()}\n")
    print("Conteo de Usuarios Activos vs Inactivos:")
    print(f"{df_limpio['Activo'].value_counts()}\n")

    # Describiendo las fechas
    print("*** DESCRIPCION DE FECHAS ***")
    print(f"Fecha de Alta más antigua: {df_limpio['FechaAlta'].min()}")
    print(f"Fecha de Alta más reciente: {df_limpio['FechaAlta'].max()}")
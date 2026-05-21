import pandas as pd

def describir_conflicto(df_limpio):
    print("*** DESCRIPCION DEL DATASET: CONFLICTO ***")
    print(f"Numero de filas del dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(df_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{df_limpio.dtypes}\n")

    # Estadísticas (Id, IDs foráneas y Monto Reclamado)
    print("*** ESTADISTICAS ***")
    print(f"{df_limpio[['Id', 'UsuarioDemandanteId', 'UsuarioDemandadoId', 'MontoReclamado']].describe()}\n")

    # Información de conteos valiosos
    print("*** CONTEOS ***")
    print("Conteo por Estado del Conflicto (ID):")
    print(f"{df_limpio['EstadoConflictoId'].value_counts()}\n")
    print("Conteo por Tipo de Conflicto (ID):")
    print(f"{df_limpio['TipoConflictoId'].value_counts()}\n")

    # Describiendo las fechas (Tiene FechaInicio y FechaCierre)
    print("*** DESCRIPCION DE FECHAS ***")
    print(f"Fecha de Inicio más antigua: {df_limpio['FechaInicio'].min()}")
    print(f"Fecha de Inicio más reciente: {df_limpio['FechaInicio'].max()}\n")
    
    # Manejo especial por si quedan todos como NULL en FechaCierre
    if df_limpio['FechaCierre'].notna().any():
        print(f"Fecha de Cierre más antigua: {df_limpio['FechaCierre'].min()}")
        print(f"Fecha de Cierre más reciente: {df_limpio['FechaCierre'].max()}")
    else:
        print("No hay fechas de cierre registradas (Todos los conflictos siguen abiertos).")
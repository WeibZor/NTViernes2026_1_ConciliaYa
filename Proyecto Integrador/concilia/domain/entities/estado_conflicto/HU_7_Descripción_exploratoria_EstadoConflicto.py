import pandas as pd


def descripcion_estado_conflicto(data_frame_limpio):

    # 1. Cantidad de registros
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")

    # 2. Cantidad de atributos
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")

    # 3. Nombres de los atributos
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")

    # 4. Tipos de dato de cada atributo
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio.dtypes}")

    # 5. Estadisticas descriptivas del campo numerico (id)
    print("*** ESTADISTICAS ***")
    print(f"{data_frame_limpio[['id']].describe()}")

    # 6. Conteos de columnas categoricas de interes
    print("*** CONTEOS ***")
    print(data_frame_limpio["nombre"].value_counts())
    print(data_frame_limpio["codigo"].value_counts())
    print(data_frame_limpio["estado"].value_counts())

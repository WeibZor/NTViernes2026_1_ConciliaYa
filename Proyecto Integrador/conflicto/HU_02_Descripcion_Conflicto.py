import pandas as pd


def descripcion_conflictos(df):
    """HU 02: Describe la tabla Conflicto para entender su estructura y calidad."""
    print("\n[HU 02] Descripción exploratoria con Pandas")

    print("\nMuestra inicial (head):")
    print(df.head())

    print("\nMuestra final (tail):")
    print(df.tail())

    print("\nInformación general (info):")
    print(df.info())

    print("\nEstadísticas básicas (describe):")
    print(df.describe(include="all"))

    columnas = list(df.columns)
    print("\nColumnas identificadas:", columnas)

    tipos = df.dtypes.to_dict()
    categoricas = [col for col, tipo in tipos.items() if tipo == "object" or tipo.name == "string"]
    numericas = [col for col, tipo in tipos.items() if tipo.kind in "ifbu"]
    fechas = [col for col, tipo in tipos.items() if "datetime" in tipo.name]

    print("\nClasificación de variables:")
    print("- Categóricas:", categoricas)
    print("- Numéricas:", numericas)
    print("- De fecha/tiempo:", fechas)

    return {
        "head": df.head(),
        "tail": df.tail(),
        "info": df.info(),
        "describe": df.describe(include="all"),
        "columnas": columnas,
        "categoricas": categoricas,
        "numericas": numericas,
        "fechas": fechas,
    }

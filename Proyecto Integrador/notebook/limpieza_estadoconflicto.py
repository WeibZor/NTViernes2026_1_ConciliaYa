import pandas as pd

# Campos del DTO: id, nombre, codigo, descripcion, activo

def limpiar_estadoConflictos(df_sucio):
    df = df_sucio.copy()

    # 1. Textos
    df["nombre"]      = df["nombre"].astype("string").str.strip().str.title()
    df["codigo"]      = df["codigo"].astype("string").str.strip().str.upper()
    df["descripcion"] = df["descripcion"].astype("string").str.strip()

    # 2. Valores esperados (descartar inyecciones del simulador)
    df["nombre"] = df["nombre"].where(
        df["nombre"].isin(["Abierto", "Cerrado", "En Proceso"]), pd.NA
    )
    df["codigo"] = df["codigo"].where(
        df["codigo"].isin(["ABR001", "CER002", "PRO003"]), pd.NA
    )

    # 3. Numéricos y booleanos
    df["id"]     = pd.to_numeric(df["id"], errors="coerce")
    df["activo"] = df["activo"].map({True: True, False: False, 1: True, 0: False})

    df = df[df["id"] > 0]

    # 4. Obligatorias
    df = df.dropna(subset=["id", "nombre", "codigo", "activo"])

    return df

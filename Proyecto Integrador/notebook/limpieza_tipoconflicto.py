import pandas as pd

# Campos del TipoConflictoDto: id, nombre, descripcion, activo

def limpiar_tipoConflicto(df_sucio):
    df = df_sucio.copy()

    # 1. Textos
    df["nombre"]      = df["nombre"].astype("string").str.strip().str.title()
    df["descripcion"] = df["descripcion"].astype("string").str.strip()

    # 2. Valores esperados
    df["nombre"] = df["nombre"].where(
        df["nombre"].isin(["Pago", "Contrato", "Servicio"]), pd.NA
    )

    # 3. Numéricos y booleanos
    df["id"]     = pd.to_numeric(df["id"], errors="coerce")
    df["activo"] = df["activo"].map({True: True, False: False, 1: True, 0: False})

    df = df[df["id"] > 0]

    # 4. Obligatorias
    df = df.dropna(subset=["id", "nombre", "descripcion", "activo"])

    return df

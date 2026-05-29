import pandas as pd

# Campos de la entidad Usuario (el controller devuelve la entidad completa):
# id, nombre, apellido, tipoDocumento, documento, correo, telefono,
# perfil: { id, nombre, descripcion, activo },
# activo, fechaAlta
#
# APLANAMIENTO: extraemos perfil.id -> perfilId  y  perfil.nombre -> perfilNombre

def limpiar_usuarios(df_sucio):
    df = df_sucio.copy()

    # --- Aplanar objeto anidado "perfil" ---
    df["perfilId"]     = df["perfil"].apply(lambda p: p["id"]     if isinstance(p, dict) else None)
    df["perfilNombre"] = df["perfil"].apply(lambda p: p["nombre"] if isinstance(p, dict) else None)
    df = df.drop(columns=["perfil"])

    # 1. Textos
    df["nombre"]        = df["nombre"].astype("string").str.strip()
    df["apellido"]      = df["apellido"].astype("string").str.strip()
    df["tipoDocumento"] = df["tipoDocumento"].astype("string").str.strip().str.upper()
    df["correo"]        = df["correo"].astype("string").str.strip().str.lower()
    df["perfilNombre"]  = df["perfilNombre"].astype("string").str.strip().str.lower()

    # 2. Valores esperados
    df["tipoDocumento"] = df["tipoDocumento"].where(
        df["tipoDocumento"].isin(["DNI", "CUIT", "PASAPORTE"]), pd.NA
    )
    df["correo"] = df["correo"].where(
        df["correo"].str.contains("@", na=False), pd.NA
    )
    df["nombre"] = df["nombre"].where(
        ~df["nombre"].isin(["INVALIDO", "clase de python"]), pd.NA
    )

    # 3. Numéricos y booleanos
    df["id"]       = pd.to_numeric(df["id"],       errors="coerce")
    df["perfilId"] = pd.to_numeric(df["perfilId"], errors="coerce")
    df["activo"]   = df["activo"].map({True: True, False: False, 1: True, 0: False})
    df["fechaAlta"] = pd.to_datetime(df["fechaAlta"], errors="coerce")

    df = df[df["id"] > 0]
    df = df[(df["perfilId"] >= 1) & (df["perfilId"] <= 10)]

    # 4. Obligatorias
    df = df.dropna(subset=["id", "nombre", "apellido", "tipoDocumento", "correo", "perfilId", "activo"])

    return df

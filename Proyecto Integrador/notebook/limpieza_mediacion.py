import pandas as pd

# Campos de la entidad Mediacion (controller devuelve entidad completa):
# id, conflicto{...}, usuarioMediador{...}, estadoConflicto{...},
# fechaProgramada, lugar, observaciones, resultado, fechaRegistro, activo
#
# APLANAMIENTO:
#   conflicto.id          -> conflictoId
#   usuarioMediador.id    -> mediadorId
#   usuarioMediador.nombre-> mediadorNombre
#   estadoConflicto.nombre-> estadoNombre

LUGARES_VALIDOS = [
    "Oficina Central Piso 2",
    "Sala Virtual Zoom",
    "Sede Norte Sala A",
    "Sede Sur Sala B"
]

def limpiar_mediacion(df_sucio):
    df = df_sucio.copy()

    # --- Aplanar objetos anidados ---
    df["conflictoId"]   = df["conflicto"].apply(lambda x: x["id"]     if isinstance(x, dict) else None)
    df["mediadorId"]    = df["usuarioMediador"].apply(lambda x: x["id"]     if isinstance(x, dict) else None)
    df["mediadorNombre"]= df["usuarioMediador"].apply(lambda x: x["nombre"] if isinstance(x, dict) else None)
    df["estadoNombre"]  = df["estadoConflicto"].apply(lambda x: x["nombre"] if isinstance(x, dict) else None)
    df = df.drop(columns=["conflicto", "usuarioMediador", "estadoConflicto"])

    # 1. Textos
    df["lugar"]         = df["lugar"].astype("string").str.strip()
    df["observaciones"] = df["observaciones"].astype("string").str.strip()
    df["resultado"]     = df["resultado"].astype("string").str.strip()
    df["estadoNombre"]  = df["estadoNombre"].astype("string").str.strip()

    df["lugar"] = df["lugar"].where(
        df["lugar"].isin(LUGARES_VALIDOS), pd.NA
    )

    # 2. Numéricos y booleanos
    df["id"]          = pd.to_numeric(df["id"],          errors="coerce")
    df["conflictoId"] = pd.to_numeric(df["conflictoId"], errors="coerce")
    df["mediadorId"]  = pd.to_numeric(df["mediadorId"],  errors="coerce")
    df["activo"]      = df["activo"].map({True: True, False: False, 1: True, 0: False})

    df = df[df["id"] > 0]
    df = df[df["conflictoId"] > 0]

    # 3. Fechas
    df["fechaProgramada"] = pd.to_datetime(df["fechaProgramada"], errors="coerce")
    df["fechaRegistro"]   = pd.to_datetime(df["fechaRegistro"],   errors="coerce")

    df["fechaProgramada"] = df["fechaProgramada"].fillna(pd.to_datetime("2026-02-01"))

    # 4. Obligatorias
    df = df.dropna(subset=["id", "conflictoId", "mediadorId", "lugar", "resultado", "activo"])

    return df

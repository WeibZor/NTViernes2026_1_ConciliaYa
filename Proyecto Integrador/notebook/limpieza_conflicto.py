import pandas as pd

# Campos de la entidad Conflicto (controller devuelve entidad completa):
# id, usuarioDemandante{...}, usuarioDemandado{...},
# tipoConflicto{...}, estadoConflicto{...},
# asunto, descripcion, fechaInicio, fechaCierre,
# resultado, montoReclamado, activo, fechaAlta
#
# APLANAMIENTO:
#   tipoConflicto.id     -> tipoConflictoId
#   tipoConflicto.nombre -> tipoConflictoNombre
#   estadoConflicto.id   -> estadoConflictoId
#   estadoConflicto.nombre -> estadoConflictoNombre
#   usuarioDemandante.id -> demandanteId
#   usuarioDemandado.id  -> demandadoId

def limpiar_conflicto(df_sucio):
    df = df_sucio.copy()

    # --- Aplanar objetos anidados ---
    df["tipoConflictoId"]      = df["tipoConflicto"].apply(lambda x: x["id"]     if isinstance(x, dict) else None)
    df["tipoConflictoNombre"]  = df["tipoConflicto"].apply(lambda x: x["nombre"] if isinstance(x, dict) else None)
    df["estadoConflictoId"]    = df["estadoConflicto"].apply(lambda x: x["id"]     if isinstance(x, dict) else None)
    df["estadoConflictoNombre"]= df["estadoConflicto"].apply(lambda x: x["nombre"] if isinstance(x, dict) else None)
    df["demandanteId"]         = df["usuarioDemandante"].apply(lambda x: x["id"] if isinstance(x, dict) else None)
    df["demandadoId"]          = df["usuarioDemandado"].apply(lambda x: x["id"]  if isinstance(x, dict) else None)
    df = df.drop(columns=["tipoConflicto", "estadoConflicto", "usuarioDemandante", "usuarioDemandado"])

    # 1. Textos
    df["asunto"]      = df["asunto"].astype("string").str.strip()
    df["descripcion"] = df["descripcion"].astype("string").str.strip()
    df["resultado"]   = df["resultado"].astype("string").str.strip()

    df["asunto"] = df["asunto"].where(
        ~df["asunto"].isin(["ASUNTO_INVALIDO", "TEST_ERROR"]), pd.NA
    )

    # 2. Numéricos y booleanos
    df["id"]               = pd.to_numeric(df["id"],               errors="coerce")
    df["montoReclamado"]   = pd.to_numeric(df["montoReclamado"],   errors="coerce")
    df["tipoConflictoId"]  = pd.to_numeric(df["tipoConflictoId"],  errors="coerce")
    df["estadoConflictoId"]= pd.to_numeric(df["estadoConflictoId"],errors="coerce")
    df["demandanteId"]     = pd.to_numeric(df["demandanteId"],     errors="coerce")
    df["demandadoId"]      = pd.to_numeric(df["demandadoId"],      errors="coerce")
    df["activo"]           = df["activo"].map({True: True, False: False, 1: True, 0: False})

    df = df[df["id"] > 0]
    df = df[df["montoReclamado"] > 0]

    # 3. Fechas
    df["fechaInicio"] = pd.to_datetime(df["fechaInicio"], errors="coerce")
    df["fechaCierre"] = pd.to_datetime(df["fechaCierre"], errors="coerce")  # puede ser null
    df["fechaAlta"]   = pd.to_datetime(df["fechaAlta"],   errors="coerce")

    df["fechaInicio"] = df["fechaInicio"].fillna(pd.to_datetime("2026-01-01"))

    # 4. Obligatorias
    df = df.dropna(subset=["id", "asunto", "tipoConflictoId", "estadoConflictoId",
                            "demandanteId", "fechaInicio", "activo"])

    return df

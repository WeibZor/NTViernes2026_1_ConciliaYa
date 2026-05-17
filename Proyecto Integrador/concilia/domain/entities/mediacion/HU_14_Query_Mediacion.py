import pandas as pd


def query_mediaciones(data_frame):
    """Aplica consultas query() sobre la tabla Mediacion y devuelve subconjuntos de datos."""
    df = data_frame.copy()
    resultados = {}

    if "estado" in df.columns and "costo" in df.columns:
        resultados["query_estado_costo"] = df.query(
            "estado == 'En proceso' and costo > 500000"
        )

    if "tipo" in df.columns and "fecha_programada" in df.columns:
        df["fecha_programada"] = pd.to_datetime(df["fecha_programada"], errors="coerce")
        resultados["query_tipo_fecha"] = df.query(
            "tipo == 'Laboral' and fecha_programada >= '2026-02-01'"
        )

    if "usuario_mediador_id" in df.columns and "costo" in df.columns:
        resultados["query_mediador_costo"] = df.query(
            "usuario_mediador_id <= 10 and costo < 300000"
        )

    return resultados

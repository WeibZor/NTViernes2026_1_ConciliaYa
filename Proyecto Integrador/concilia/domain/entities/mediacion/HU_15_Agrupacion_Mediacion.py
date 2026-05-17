import pandas as pd


def agrupar_mediaciones(data_frame):
    """Realiza agrupaciones y métricas agregadas sobre la tabla Mediacion."""
    df = data_frame.copy()
    resultados = {}

    if "estado" in df.columns and "costo" in df.columns:
        resultados["estado_resumen"] = (
            df.groupby("estado", dropna=False)
            .agg(
                registros=("id", "count"),
                costo_promedio=("costo", "mean"),
                costo_total=("costo", "sum"),
                costo_minimo=("costo", "min"),
                costo_maximo=("costo", "max")
            )
            .reset_index()
        )

    if "tipo" in df.columns and "usuario_mediador_id" in df.columns:
        resultados["tipo_mediador"] = (
            df.groupby(["tipo", "usuario_mediador_id"], dropna=False)
            .agg(
                registros=("id", "count"),
                costo_promedio=("costo", "mean"),
                fecha_ultima=("fecha_registro", "max")
            )
            .reset_index()
        )

    if "lugar" in df.columns and "estado" in df.columns:
        resultados["lugar_estado"] = (
            df.groupby(["lugar", "estado"], dropna=False)
            .agg(
                registros=("id", "count"),
                monto_total=("costo", "sum")
            )
            .reset_index()
        )

    return resultados

import pandas as pd


def agrupaciones_perfil(df):
    """HU 20: Agrupa información de Perfil para obtener resúmenes y métricas."""
    print("\n[HU 20] Agrupación y resumen de datos")

    resumen_nombre_activo = (
        df.groupby(["nombre", "activo"], dropna=False)
        .agg(
            perfiles=("id", "count"),
            id_promedio=("id", "mean"),
            fecha_min=("fecha", "min"),
            fecha_max=("fecha", "max"),
        )
        .reset_index()
    )
    print("\nResumen por nombre y activo:")
    print(resumen_nombre_activo)

    resumen_descripcion = (
        df.groupby("descripcion", dropna=False)
        .agg(
            perfiles=("id", "count"),
            nombres_distintos=("nombre", "nunique"),
        )
        .reset_index()
    )
    print("\nResumen por descripcion:")
    print(resumen_descripcion)

    return {"por_nombre_activo": resumen_nombre_activo, "por_descripcion": resumen_descripcion}
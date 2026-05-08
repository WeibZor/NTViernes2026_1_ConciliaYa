def agrupaciones_tipos_conflicto(df):
    """HU 25: Agrupa información de TipoConflicto para obtener resúmenes y métricas."""
    print("\n[HU 25] Agrupación y resumen de datos")

    resumen_activo = (
        df.groupby("Activo", dropna=False)
        .agg(
            tipos=("Id", "count"),
            id_promedio=("Id", "mean"),
            fecha_min=("FechaAlta", "min"),
            fecha_max=("FechaAlta", "max"),
        )
        .reset_index()
    )
    print("\nResumen por Activo:")
    print(resumen_activo)

    resumen_nombre = (
        df.groupby("Nombre", dropna=False)
        .agg(
            tipos=("Id", "count"),
            usuarios_alta_distintos=("UsuarioAltaId", "nunique"),
        )
        .reset_index()
    )
    print("\nResumen por Nombre:")
    print(resumen_nombre)

    return {"por_activo": resumen_activo, "por_nombre": resumen_nombre}
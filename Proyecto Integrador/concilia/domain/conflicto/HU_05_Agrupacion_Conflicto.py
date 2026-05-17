def agrupaciones_conflicto(df):
    """HU 05: Agrupa información de Conflicto para obtener resúmenes y métricas."""
    print("\n[HU 05] Agrupación y resumen de datos")

    agrupacion_estado = (
        df.groupby("Estado", dropna=False)
        .agg(
            conflictos=("Id", "count"),
            usuarios_distintos=("UsuarioId", "nunique") if "UsuarioId" in df.columns else ("Id", "nunique"),
        )
        .reset_index()
    )
    print("\nResumen por Estado:")
    print(agrupacion_estado)

    agrupacion_tipo = (
        df.groupby("Tipo Conflicto", dropna=False)
        .agg(
            conflictos=("Id", "count"),
            fecha_min=("FechaAlta", "min") if "FechaAlta" in df.columns else ("Id", "min"),
        )
        .reset_index()
    )
    print("\nResumen por Tipo Conflicto:")
    print(agrupacion_tipo)

    return {"por_estado": agrupacion_estado, "por_tipo": agrupacion_tipo}

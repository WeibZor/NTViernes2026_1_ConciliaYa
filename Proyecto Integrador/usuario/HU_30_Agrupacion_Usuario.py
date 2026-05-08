def agrupaciones_usuario(df):
    """HU 30: Agrupa información de Usuario para obtener resúmenes y métricas."""
    print("\n[HU 30] Agrupación y resumen de datos")

    resumen_perfil = (
        df.groupby(["PerfilId", "Activo"], dropna=False)
        .agg(
            usuarios=("Id", "count"),
            id_promedio=("Id", "mean"),
            fecha_min=("FechaAlta", "min"),
            fecha_max=("FechaAlta", "max"),
        )
        .reset_index()
    )
    print("\nResumen por PerfilId y Activo:")
    print(resumen_perfil)

    resumen_documento = (
        df.groupby("TipoDocumento", dropna=False)
        .agg(
            usuarios=("Id", "count"),
            perfiles_distintos=("PerfilId", "nunique"),
        )
        .reset_index()
    )
    print("\nResumen por TipoDocumento:")
    print(resumen_documento)

    return {"por_perfil_activo": resumen_perfil, "por_tipo_documento": resumen_documento}

import pandas as pd


def consultas_conflicto(df):
    """HU 04: Filtra la tabla Conflicto con query() para obtener subconjuntos de interés."""
    print("\n[HU 04] Transformación con query()")

    q1 = df.query("Activo == True") if "Activo" in df.columns else df.head(0)
    print("\nConsulta 1: registros activos")
    print(q1.head())
    print(f"Registros encontrados: {len(q1)}")

    q2 = df.query("`Tipo Conflicto` == 'Laboral'") if "Tipo Conflicto" in df.columns else df.head(0)
    print("\nConsulta 2: tipo de conflicto = Laboral")
    print(q2.head())
    print(f"Registros encontrados: {len(q2)}")

    fecha_col = next((col for col in df.columns if "fecha" in col.lower()), None)
    if fecha_col is not None:
        fecha_limite = pd.Timestamp.now() - pd.Timedelta(days=180)
        q3 = df.query(f"`{fecha_col}` >= @fecha_limite")
    else:
        q3 = df.head(0)
    print("\nConsulta 3: registros recientes de los últimos 180 días")
    print(q3.head())
    print(f"Registros encontrados: {len(q3)}")

    return {"activos": q1, "tipo_laboral": q2, "recientes": q3}

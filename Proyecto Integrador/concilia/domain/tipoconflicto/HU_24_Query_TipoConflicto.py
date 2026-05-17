import pandas as pd


def consultas_tipos_conflicto(df):
    """HU 24: Filtra la tabla TipoConflicto con query() para obtener subconjuntos de interés."""
    print("\n[HU 24] Transformación de datos con query()")

    q1 = df.query("Activo == True")
    print("\nConsulta 1: Tipos de conflicto activos")
    print(q1.head(5))
    print(f"Registros encontrados: {len(q1)}")

    q2 = df.query("Nombre == 'Laboral'")
    print("\nConsulta 2: Tipos de conflicto con nombre 'Laboral'")
    print(q2.head(5))
    print(f"Registros encontrados: {len(q2)}")

    fecha_limite = pd.Timestamp.now() - pd.Timedelta(days=180)
    q3 = df.query("FechaAlta >= @fecha_limite")
    print("\nConsulta 3: Tipos de conflicto creados en los últimos 180 días")
    print(q3.head(5))
    print(f"Registros encontrados: {len(q3)}")

    return {"activos": q1, "laborales": q2, "ultimos_180_dias": q3}

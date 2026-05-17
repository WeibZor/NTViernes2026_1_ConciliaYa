import pandas as pd


def consultas_perfil(df):
    """HU 19: Filtra la tabla Perfil con query() para obtener subconjuntos de interés."""
    print("\n[HU 19] Transformación de datos con query()")

    q1 = df.query("activo == True and nombre == 'administrador'")
    print("\nConsulta 1: Perfiles activos de administrador")
    print(q1.head(5))
    print(f"Registros encontrados: {len(q1)}")

    q2 = df.query("nombre == 'usuario' and descripcion.str.contains('acceso', na=False)")
    print("\nConsulta 2: Perfiles de usuario con descripciones que contienen 'acceso'")
    print(q2.head(5))
    print(f"Registros encontrados: {len(q2)}")

    fecha_limite = pd.Timestamp("2026-06-01")
    q3 = df.query("fecha >= @fecha_limite")
    print("\nConsulta 3: Perfiles creados desde junio de 2026")
    print(q3.head(5))
    print(f"Registros encontrados: {len(q3)}")

    return {"activos_admin": q1, "usuarios_acceso": q2, "desde_junio": q3}

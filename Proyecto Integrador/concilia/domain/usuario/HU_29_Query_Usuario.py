import pandas as pd


def consultas_usuario(df):
    """HU 29: Filtra la tabla Usuario con query() para obtener subconjuntos de interés."""
    print("\n[HU 29] Transformación de datos con query()")

    q1 = df.query("Activo == True and PerfilId == 1")
    print("\nConsulta 1: Usuarios activos con perfil de administrador")
    print(q1.head(5))
    print(f"Registros encontrados: {len(q1)}")

    q2 = df.query("TipoDocumento == 'DNI' and PerfilId == 2")
    print("\nConsulta 2: Usuarios con documento DNI y perfil usuario")
    print(q2.head(5))
    print(f"Registros encontrados: {len(q2)}")

    fecha_limite = pd.Timestamp.now() - pd.Timedelta(days=90)
    q3 = df.query("FechaAlta >= @fecha_limite")
    print("\nConsulta 3: Usuarios creados en los últimos 90 días")
    print(q3.head(5))
    print(f"Registros encontrados: {len(q3)}")

    return {"activos_admin": q1, "dni_usuarios": q2, "ultimos_90_dias": q3}

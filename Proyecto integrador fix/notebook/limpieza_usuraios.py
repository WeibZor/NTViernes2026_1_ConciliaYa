import pandas as pd

def limpiar_usuarios(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpieza de textos (espacios y minúsculas)
    df_limpio["Nombre"] = df_limpio["Nombre"].astype("string").str.strip()
    df_limpio["Apellido"] = df_limpio["Apellido"].astype("string").str.strip()
    df_limpio["TipoDocumento"] = df_limpio["TipoDocumento"].astype("string").str.strip().str.upper()
    df_limpio["Documento"] = df_limpio["Documento"].astype("string").str.strip()
    df_limpio["Correo"] = df_limpio["Correo"].astype("string").str.strip().str.lower()

    # 2. Controlar valores inesperados en TipoDocumento
    valores_esperados_doc = ["DNI", "CUIT", "PASAPORTE"]
    df_limpio["TipoDocumento"] = df_limpio["TipoDocumento"].where(
        df_limpio["TipoDocumento"].isin(valores_esperados_doc),
        pd.NA
    )
    
    # 3. Controlar correos inválidos simulados
    df_limpio["Correo"] = df_limpio["Correo"].where(
        df_limpio["Correo"].str.contains("@", na=False),
        pd.NA
    )

    # 4. Limpieza de datos numéricos y booleanos
    df_limpio["Id"] = pd.to_numeric(df_limpio["Id"], errors='coerce')
    df_limpio["PerfilId"] = pd.to_numeric(df_limpio["PerfilId"], errors='coerce')
    df_limpio["UsuarioAltaId"] = pd.to_numeric(df_limpio["UsuarioAltaId"], errors='coerce')
    df_limpio["Activo"] = df_limpio["Activo"].map({True: True, False: False, 1: True, 0: False})

    # Verificación de rangos numéricos válidos
    df_limpio = df_limpio[df_limpio["Id"] > 0]
    df_limpio = df_limpio[(df_limpio["PerfilId"] >= 1) & (df_limpio["PerfilId"] <= 5)]

    # 5. Limpieza de Fechas
    df_limpio["FechaAlta"] = pd.to_datetime(df_limpio["FechaAlta"], errors='coerce')
    fecha_default = pd.to_datetime("2026-01-15")
    df_limpio["FechaAlta"] = df_limpio["FechaAlta"].fillna(fecha_default)

    # 6. Descartar filas con nulos en columnas obligatorias
    columnas_obligatorias = ["Id", "Nombre", "Apellido", "TipoDocumento", "Documento", "Activo"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    return df_limpio
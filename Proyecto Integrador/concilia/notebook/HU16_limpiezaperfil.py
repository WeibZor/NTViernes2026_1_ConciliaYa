
import pandas as pd

def limpiar_perfil(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    columnas_texto=["nombre", "descripcion"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #valores esperados del nombre del perfil.
    nombres_esperados=["administrador", "gestor", "usuario"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(
        
         data_frame_limpio["nombre"].isin(nombres_esperados),
         pd.NA
         )
    #valores esperados de las descripciones de perfil
    descripciones_esperadas=["acceso total al sistema","acceso limitado a ciertas funciones",
                       "acceso restringido a datos sensibles", "acceso a reportes y estadísticas",
                       "acceso a configuraciones del sistema","acceso a herramientas de administración",
                       "acceso a recursos compartidos","acceso a información de contacto",
                       "acceso a documentos internos","acceso a foros y discusiones"]
    
    data_frame_limpio["descripcion"]=data_frame_limpio["descripcion"].where(

        data_frame_limpio["descripcion"].isin(descripciones_esperadas),
        pd.NA

    )


    #valores activo

    activo_esperado=[True, False]

    data_frame_limpio["activo"]=data_frame_limpio["activo"].where(

        data_frame_limpio["activo"].isin(activo_esperado),
        pd.NA

    )

    #numeros (id)

    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])

    #numericos permitidos
    
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"] > 0]


    #fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])

    #fecha por defecto si el campo llega vacio
    fecha_Default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_Default)    


    #novedades
    columnas_obligatorias=["id", "nombre", "descripcion", "activo", "fecha"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio = data_frame_limpio.drop_duplicates()
    
    return data_frame_limpio
    
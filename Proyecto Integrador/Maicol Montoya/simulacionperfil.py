import random
from datetime import datetime, timedelta
def generarPerfil(numeroPerfiles):


    listaNombre =["Administrador", "Gestor", "Usuario", "Administrador", "Gestor", "Usuario", 
                  "Administrador", "Gestor", "Usuario", "Administrador"]


    listaDescripcion =["Acceso total al sistema", "Acceso limitado a ciertas funciones",
                        "Acceso restringido a datos sensibles", "Acceso a reportes y estadísticas"
                        , "Acceso a configuraciones del sistema", "Acceso a herramientas de administración"
                        , "Acceso a recursos compartidos", "Acceso a información de contacto", 
                        "Acceso a documentos internos", "Acceso a foros y discusiones"]

    listaBoolean = [True, False]

    fechaInicio=datetime(2026, 1, 1)



    perfiles=[]

    for _ in range(numeroPerfiles):

        fecha=fechaInicio + timedelta(days=random.randint(0, 365))

        perfil={
            "id": random.randint(1, 100),
            "nombre": random.choice(listaNombre),
            "descripcion": random.choice(listaDescripcion),
            "activo": random.choice(listaBoolean),
            "fecha": fecha.strftime("%Y-%m-%d")
        }    
        perfiles.append(perfil)
    return perfiles
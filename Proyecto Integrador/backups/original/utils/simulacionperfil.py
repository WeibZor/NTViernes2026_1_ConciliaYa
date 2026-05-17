
#08/05/2026 se hizo cambio en las mayusculas de la listaNombre Y la ListaDescripcion, tambien se añadieron los ERRORES controlados.

import random
from datetime import datetime, timedelta
def generarPerfil(numeroPerfiles):


    listaNombre =["administrador", "gestor", "usuario"]



    listaDescripcion =["acceso total al sistema","acceso limitado a ciertas funciones",
                       "acceso restringido a datos sensibles", "acceso a reportes y estadísticas",
                       "acceso a configuraciones del sistema","acceso a herramientas de administración",
                       "acceso a recursos compartidos","acceso a información de contacto",
                       "acceso a documentos internos","acceso a foros y discusiones"]

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



        #ERRORES CONTROLADOS
        probabilidadError=random.random()

        if probabilidadError < 0.1:
            perfil["id"]= random.choice([0,-1,None])
            perfil["activo"]=None
        elif probabilidadError < 0.3:
            perfil["descripcion"]= random.choice(["no hay acceso","no tienes permiso", "no te dejo entrar"])
            perfil["descripcion"]=" " + perfil["descripcion"]+" "
        elif probabilidadError < 0.6:
            perfil["descripcion"]= None
            perfil["nombre"]= random.choice(["samuel", "tomas", "no hay nombre", None])
        elif probabilidadError < 0.9:
            perfil["fecha"]=None
         
         
        
        perfiles.append(perfil)
    return perfiles

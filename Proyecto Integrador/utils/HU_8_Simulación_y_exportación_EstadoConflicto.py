import random as rd

def generar_estadoConflictos(num_estadoConflictos):

    listaNombres=["abierto","cerrado","Proceso"]

    listaCodigos=["ABR001","CER002","PRO003"]

    listaActivo=["True","False"]

    listaDescripcion=["abierto por inconvenientes","cerrado y finalizado","en proceso por demora"]

    estadosClonfictos=[]

    for _ in range (num_estadoConflictos):
        estadoConflicto={
            "id":rd.randint(0,100),
            "nombre":rd.choice(listaNombres),
            "codigo":rd.choice(listaCodigos),
            "estado":rd.choice(listaActivo),
            "descripcion":rd.choice(listaDescripcion)
        }
        probabilidadError=rd.random()
        if(probabilidadError<0.2):
            estadoConflicto["id"]=None
        elif(probabilidadError<0.4):
            estadoConflicto["nombre"]=rd.choice(["MedioCerrado","MedioAbierto"])
        elif(probabilidadError<0.5):
            estadoConflicto=rd.choice([1,1000,2])
        elif(probabilidadError<0.8):
            estadoConflicto["descripcion"]=" "+estadoConflicto["descripcion"].upper()
            
        estadosClonfictos.append(estadoConflicto)
    return estadosClonfictos

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
        estadosClonfictos.append(estadoConflicto)
    return estadosClonfictos

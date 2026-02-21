#crear una lista de 20 notas
import random
def CrearListaDeNotas(cantidadNotas):
    notas=[]
    for _ in range(cantidadNotas):
        nota=random.randint(1,5)
        notas.append(nota)
    return notas    

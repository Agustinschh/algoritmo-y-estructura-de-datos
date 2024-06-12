##Desarrollar una función recursiva que permita listar los elementos de vector/lista de
#manera inversa al que están cargados. Preferentemente la función solo debe tener un parámetro que es la lista de elementos.

def inversa(lista):
    if lista ==[]:
        return ("la lista esta vacia")
    else:
        inversa(lista[1:])
        print(lista[0])

# Ejemplo de uso
ejemplo = [23,54,65,28,53,85,53]
inversa(ejemplo)
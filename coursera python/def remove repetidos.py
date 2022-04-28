
def remove_repetidos(lista):
    lista2 = []
    for numero in lista:
        if numero not in lista2:
            lista2.append(numero)
    lista2.sort()
    return lista2

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

lista = remove_repetidos(lista)
print (lista)
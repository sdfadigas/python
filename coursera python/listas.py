""" # imprime todos os elementos na ordem inversa 
flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1

aluno = ["Fulano de Tal", 25, "Rua xyz, 123", "São Paulo", 3, "Matemática", 7.5, "Português", 6.6, "Artes", 10]
aluno[1]=aluno[1]+1
print(aluno)


animais = ["gato", "cachorro", "vaca", "cavalo", "casa"]
animais.append("cobra")
print(animais)

for x in (animais):
    print("eu gosto de ", x)
pares = range (10, 20, 2)
for y in pares:   print(y)

lista = [1,2,5,4,6,4,6,4,87,413,4,47]
for z in range(len(lista)):
    lista[z] = lista[z]**2
print(lista)
print(z)

animais = ["gato", "cachorro", "papagaio",
"arara", "jacaré"]
for x in animais:
    print("--> ", x)

lista1 = ["eu","tu","nós"]
lista2 = lista1[:]
lista2[0] = "ele"
print(lista1)
print(lista2)

if "nos" in lista1:
    print ("sim")
else:
    print("nops")

print([3,4,1,3,5]+[2,7,9,5,6]) """

""" alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letras = alfabeto[1:10]
print(letras)
print(len(letras))
print(alfabeto[0:13])
print(len(alfabeto[0:13]))

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra")
print(carnes2)
print(carnes) """

""" carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2) """

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")

carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1
print(carnes3)

pares = [2, 4, 6, 8, 10]
x = pares * 3
print(x)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])
print(carnes)
print(x)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]
if lista3 is lista2:
    print("yes")
else:
    print("no")

a = "cavalo"
b = "cachorro"
c = "gato"
d = "cachorro"

if d is b:
 print("yes")

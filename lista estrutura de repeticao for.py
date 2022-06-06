#QUESTÃO 1: Faça um programa que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.
dentro=0
fora=0
for x in range(0,10):
    x=float(input("Digite um número : "))
    if(x>=10 and x<=20):
        dentro=dentro + 1
    else:
        fora=fora + 1
print("a quantidade de números digitados dentro do intervalo [10,20] é igual a ", dentro)
print("a quantidade de números fora do intervalo [10,20] é igual a ", fora)

#QUESTÃO 2: Crie um programa para contar a quantidade de números pares e ímpares de uma série de números. • numeros = (1, 2, 14, 4, 5, 6, 7, 8, 10)
par=0
impar=0
x = (1, 2, 14, 4, 5, 6, 7, 8, 10)
for i in x:
    if i % 2 == 0:
        par=par+1
    else:
        impar=impar+1

print("a sequencia possui", par, "números pares e", impar, "números ímpares")

#QUESTÃO 3: Crie um programa que receba uma string como entrada e mostre a quantidade de números e letras. Caso não seja letra ou número, ignore.
frase = str(input("digite qualquer coisa: "))
numero = 0
letra = 0
for i in frase:
    if i.isdigit():
        numero = numero + 1
    elif i.isalpha():
        letra = letra + 1

print("a quantidade de números na frase é igual a", numero, "e a quantidade de letras na frase é igual a", letra)

#QUESTÃO 4: Escreva um programa para encontrar o fatorial de qualquer número.
x=int(input("digite um número inteiro positivo ou zero: "))
fatorial = 1
for i in range(1, x + 1):
    fatorial = fatorial * i
print("O fatorial desse número é igual a: ", fatorial)
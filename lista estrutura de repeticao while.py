#QUESTÃO 1:Faça um programa, que lê um número n e imprime o Fibonacci desse número.
n = int(input("Digite um número: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    i=3
    while i <= n:
        numero = ultimo + penultimo
        penultimo = ultimo
        ultimo = numero
        i=i+1
    print("o Fibonacci desse número é", numero)
#QUESTÃO 2:Faça um programa, que lê um número n e imprime os n primeiros números da sequência de Fibonacci.
n = int(input("Digite um número: "))
print("esses são os primeiros números da sequencia de Fibonacci do número digitado:")
num1, num2 = 0, 1
i = 0
while i < n:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    i = i+1
    print(num1)
#QUESTÃO 3: Faça um programa, que lê um número n e imprime a sequência de Fibonacci até o Fibonacci do número digitado.
n = int(input("Digite o numero que deseja a sequencia Fibonacci: "))
prox=1
ant=0
if (n==0) :
  print(ant, end = ", ")
elif (n==1):
  print(prox, end = ", ")
else: 
  print(ant,prox,end = (', '))
  i=2
while i in range(n):
  termo = prox + ant
  ant = prox
  prox = termo
  i=i+1
  print(termo, end = ', ')
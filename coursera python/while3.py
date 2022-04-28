x = int(input("Digite um número inteiro: "))
i = 0
while (x != 0):
    y = x % 10
    x = (x - y)//10
    i = i + y
print(i)

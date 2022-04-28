x=int(input("digite: "))
def primo(x):
    i = 2
    while x % i != 0 and i <= x / 2:
        i = i + 1
    if x % i == 0:
        return False
    else:
        return True
def maior_primo(n):
    maior_numero = 0
    i = 2
    while i <= n:
        if primo(i):
            print(i)
            maior_numero = i
        i = i + 1
    return maior_numero


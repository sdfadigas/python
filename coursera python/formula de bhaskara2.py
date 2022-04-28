import math
def delta(a,b,c):
    return b**2-4*a*c
def main():
    a = float(input("digite o valor de a: "))
    b = float(input("digite o valor de b: "))
    c = float(input("digite o valor de c: "))
    imprime_raizes(a,b,c)
def imprime_raizes(a,b,c):
    d=delta(a,b,c)
    if d==0:
        raíz1=(-b+math.sqrt(d))/(2*a)
        print("a unica raíz é: ", raíz1)
    else:
        if d<0:
            print("esta equação não possui raizes reais")
        else:
            raíz1 = (-b+math.sqrt(d))/(2*a)
            raíz2 = (-b-math.sqrt(d))/(2*a)
            print ("a primeira raíz é: ", raíz1)
            print ("a segunda raíz é: ", raíz2)
main() 
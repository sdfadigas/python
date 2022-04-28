import math
a = float(input("digite o valor de 'a' diferente de zero: "))
b = float(input("digite o valor de 'b': "))
c = float(input("digite o valor de 'c': "))
delta = b**2 - 4*a*c
if delta < 0:
    print("esta equação não possui raízes reais")
if delta == 0:
    raíz1=(-b+math.sqrt(delta))/2*a
    print("a raiz dupla desta equação é ", raíz1)
if delta > 0:
    raíz1=(-b+math.sqrt(delta))/2*a
    raíz2=(-b-math.sqrt(delta))/2*a  
    print("as raízes da equação são ", raíz2, "e", raíz1)

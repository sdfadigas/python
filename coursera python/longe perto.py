import math
x1 = float(input("digite um número: "))
x2 = float(input("digite outro número: "))
y1 = float(input("digite mais um número: "))
y2 = float(input("digite mais um: "))
distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if distancia >= 10:
    print ("longe")
else:
    print ("perto")
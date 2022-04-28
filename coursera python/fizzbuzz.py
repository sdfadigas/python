x=float(input("digite um número:"))
sobra = x%5
sobra2 = x%3
if sobra==0 and sobra2==0 :
    print("FizzBuzz")
else:
    print(x)
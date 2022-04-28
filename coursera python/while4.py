l = int(input('digite a largura: '))
a = int(input('digite a altura: '))

while  a > 0:
   aux = 0
   while aux < l:
     print('#',end="")
     aux+=1  
   a-=1
   print()
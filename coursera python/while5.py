def PegarEntrada():
    return int(input("Forneça o um número inteiro: "))

def RetanguloVazado(dimensoes):
    largura, altura = dimensoes
    preencherVertical = 1

    while preencherVertical <= altura:
        preencherHorizontal = 1

        while preencherHorizontal <= largura:
           
            pontoCartesiano = (preencherHorizontal, preencherVertical)

           
            if pontoCartesiano[1] == 1 or pontoCartesiano[1] == altura:
                print("#", end="")
          
            elif pontoCartesiano[0] == 1 or pontoCartesiano[0] == largura:
                print("#", end="")
          
            else:
                print(" ", end="")

            preencherHorizontal += 1

        print("")
        preencherVertical += 1


def Main():
    dimensoes = (PegarEntrada(), PegarEntrada())
    RetanguloVazado(dimensoes)

Main()
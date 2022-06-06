#01 Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias_alunos = []
alunos_acima_media = 0

for aluno in range(10):
    soma_das_notas = 0
    
    for nota in range(4):
        print("Digite a ", nota+1, "ª nota do ", aluno+1, "º aluno", sep="")
        soma_das_notas += float(input())
    
    medias_alunos.append(soma_das_notas/4)
    
    if medias_alunos[aluno] >= 7.0:
        alunos_acima_media += 1
        
print("Médias dos alunos:", medias_alunos)
print("Número de alunos acima da média:", alunos_acima_media)

#02 Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outros listas.
lista1 = []
lista2 = []
lista3 = []

for elemento in range(0, 10):
    lista1.append(int(input("Digite um elemento: ")))
    
for elemento in range(0, 10):
    lista2.append(int(input("Digite um elemento: ")))
    
for elemento in range(0, 10):
    lista3.append(lista1[elemento])
    lista3.append(lista2[elemento])

print(lista3)

#03 Altere o programa anterior, intercalando 3 listas de 10 elementos cada.
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for elemento in range(0, 10):
    lista1.append(int(input("Digite um elemento: ")))
    
for elemento in range(0, 10):
    lista2.append(int(input("Digite um elemento: ")))

for elemento in range(0, 10):
    lista3.append(int(input("Digite um elemento: ")))
    
for elemento in range(0, 10):
    lista4.append(lista1[elemento])
    lista4.append(lista2[elemento])
    lista4.append(lista3[elemento])
print(lista4)



#04 Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura = []

for m in range(0, len(meses)):
    temperatura.append(float(input("Digite a temperatura do mês de " + meses[m] + ": ")))

mediaAnual = sum(temperatura)/len(temperatura)
print("Os meses que tiveream temperatura acima da média anual foram: ")
for m in range(0, len(temperatura)):
    if temperatura[m] > mediaAnual:

        print (str(m+1) + " - " + meses[m])


#05 Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
'''a. "Telefonou para a vítima?"
   b. "Esteve no local do crime?"
   c. "Mora perto da vítima?"
   d. "Devia para a vítima?"
   e. "Já trabalhou com a vítima?"'''
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print("Interrogatório policial: ")
quantidade_positivo = 0
status = {2: "Suspeito(a)",
          3: "Cúmplice",
          4: "Cúmplice",
          5: "Assassino"}

lista_perguntas = ["Telefonou para a vítima?",
                   "Esteve no local do crime?",
                   "Mora perto da vítima?",
                   "Devia para a vítima?",
                   "Já trabalhou com a vítima?"]

for i in range(len(lista_perguntas)):
    print(lista_perguntas[i] + " (responda apenas com sim ou não).")

    resposta = input("Resp.:")

    if resposta.lower() == "sim":
        quantidade_positivo += 1

if quantidade_positivo in status:
    print(status[quantidade_positivo])
else:
    print("Inocente")

#06 Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
'''a) O modelo do carro mais econômico;
   b) Quantos litros de combustível cada um dos carros cadastrados consomepara percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.'''

print('Comparativo de consumo de combustível:')
carros = []
consumo = []
preco_gasolina = 2.25
distancia_percorrida = 1000
for i in range(0, 5):
    carros.append(input('Digite o modelo do carro: '))
    consumo.append(float(input('Digite o consumo do carro km/l: ')))
print("Relatório de consumo: ")
for i in range (0, 5):
    qtd_l = round(1000 / consumo[i], 2)
    qtd_rs = round(1000 / consumo[i] * preco_gasolina, 2)
    print(f'{i+1} - {carros[i]} - {consumo[i]} - {qtd_l} - R${qtd_rs}')
print(f'O carro mais economico e: {carros[consumo.index(max(consumo))]}')

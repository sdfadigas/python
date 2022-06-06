#01 Faça uma função que receba dois números a e b e diga qual deles é o maior ou se são iguais.
a=float(input('digite um numero qualquer: '))
b=float(input('digite outro número qualquer: '))
def maior (a, b):
    if a < b:
      print(b)
    elif a > b:
      print(a)
    else:
      print("Os números são iguais.")
maior(a,b)

#02 Faça uma função que receba dois números a e b e um número limite e informe quantos desses dois números são maiores que o limite.
a=float(input('digite um numero qualquer: '))
b=float(input('digite outro número qualquer: '))
c=float(input('digite um número limite: '))
def limite():
  if a > c and b > c:
    print('os dois numeros não maiores que o limite')
  elif a > c:
    print ('apenas {} está acima do limite'.format(a))
  elif b > c:
    print ('apenas {} está acima do limite'.format(b))
  else:
    print('nenhum deles está acima do limite')
limite()


#03 Faça uma função que receba um texto e uma letra e informe quantas vezes a letra aparece no texto.
frase = input('escreva uma frase ou texto qualquer : ')
letra = input('informe a letra que você quer saber quantas vezes aparece no texto : ')
def countLetra(letra, frase):
    count = 0
    for i in range(len(frase)):
        if(frase[i] == letra):
            count = count + 1
    return count
freq = countLetra(letra, frase)
print('a quantidade de vezes que a letra {}, sem acento ou sinal gráfico, aparece no texto é de {} vezes'.format(letra,freq))

#04 Faça um programa de implemente um jogo de Dados. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random	
def rolaDado():

	_= input("aperte enter pra começar seu jogo ")
	dado1 = random.randrange(1, 7)
	dado2 = random.randrange(1, 7)
	return (dado1, dado2)

def rolaDois(dados):
	dado1, dado2 = dados
	print("o valores dos dados foram {} e {} e a soma dos valores foi igual a {}".format(dado1, dado2, sum(dados)))

value = rolaDado()
rolaDois(value)

somaDados = sum(value)

if somaDados in (7, 11):
	result = "você venceu :)"

elif somaDados in (2, 3, 12):
	result = "você perdeu :("
else:
	result = "continue jogando"
	currentpoint = somaDados
	print("sua pontuação atual é: ", currentpoint)

while result == "continue jogando":
	value = rolaDado()
	rolaDois(value)
	somaDados = sum(value)
	
	if somaDados == currentpoint:
		result = "você venceu :)"
	
	elif somaDados == 7:
		result = "você perdeu :("

if result == "você venceu :)":
	print("você venceu :)")
	
else:
	print("você perdeu :(")


#05 Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
n=int(input('digite um numero inteiro: '))
def quantDigitos(n):
    n = abs(int(n))
    if n < 2:
        return 1
    count = 0
    valor = 1
    while valor <= n:
        valor *= 10
        count += 1
    return count 
print(quantDigitos(n))

#06 Faça uma função que retorne o reverso de um número inteiro informado.Por exemplo: 127 -> 721.
n=int(input('digite um número inteiro qualquer: '))
resInverso=0
def inverso(n):
  global resInverso
  if n>0:
    resInverso=(resInverso*10)+(n%10)
    inverso(n//10)
  return resInverso
resInverso=inverso(n)
print('o inverso do número digitado é {}'.format(resInverso))

#07 Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Além disso,valide a data e informe caso a data seja inválida.

#teste de validação da data
data = input('Digite um data no formato DD/MM/YYYY: ')
dia, mes, ano = map(int, data.split('/'))
valida = False

if (mes == '01' or mes == '03' or mes == '05' or mes == '07' or \
mes == '08' or mes == '10' or mes == '12'):
  if (dia <= 31):
    valida = True

elif (mes == '04' or mes == '06' or mes == '09' or mes == '11'):
  if (dia <= 30):
    valida = True

elif mes == '02':
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if (dia <= 29):
      valida = True
elif (dia <= 28):
  valida = True

#se a data for válida, aplicar a função da data por extenso
if (valida):
  def data_por_extenso(data):
    data_a = data.split('/')
    dia = data_a[0]
    mes = data_a[1]
    ano = data_a[2]

    meses = {
        '01': 'Janeiro',
        '02': 'Fevereiro',
        '03': 'Março',
        '04': 'Abril',
        '05': 'Maio',
        '06': 'Junho',
        '07': 'Julho',
        '08': 'Agosto',
        '09': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }
    mes_extenso = meses[mes]
    return f'{dia} de {mes_extenso} de {ano}'
else:
  print('Inválida')
resultado = data_por_extenso(data)
print(resultado)

import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print('le_textos()', texto)
    return textos
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)
def separa_palavras(frase):
    return frase.split()
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)
def compara_assinatura(as_a, as_b):
    i = 0
    cp = 0
    while i < 6:
        cp = cp + abs(as_a[i]-as_b[i])
        i += 1
    cp = abs(cp)/6
    return cp
def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    #print('|sentencas:', len(sentencas))
    si = 0
    frases = []
    while si < len(sentencas):
        frases = frases + separa_frases(sentencas[si])
        si += 1
    #print('|frases:', len(frases))
    palavras = separa_palavras(chngcarac(texto))
    #print('|palavras:', len(palavras))
    unicas = n_palavras_unicas(palavras)
    #print('|unicas:', unicas)
    diferentes = n_palavras_diferentes(palavras)
    #print('|diferentes:', diferentes)
    tamPalavras = 0
    for palavra in palavras:
        tamPalavras = tamPalavras + len(palavra)
    #print('|tamPalavras', tamPalavras)
    mediaPalavras = tamPalavras/len(palavras)
    #print('|1-mediaPalavras:', mediaPalavras)
    typeToken = diferentes/len(palavras)
    #print('|2-typeToken:', typeToken)
    hapax = unicas/len(palavras)
    #print('|3-hapax:', hapax)
    tamSentenca = 0
    si = 0
    while si < len(sentencas):
        for sentenca in sentencas[si]:
            tamSentenca = tamSentenca + len(sentenca)
        si += 1
    mediaSentecas = tamSentenca/len(sentencas)
    #print('|4-mediaSentecas', mediaSentecas, tamSentenca, len(sentencas))
    complx = len(frases)/len(sentencas)
    #print('|5-complx:', complx, len(frases))
    si = 0
    medFrase = 0
    while si < len(frases):
        medFrase = medFrase + len(frases[si])# 413/9 45.88
        si += 1
    mediaFrases = medFrase/len(frases)
    #print('|6-medFrase:', mediaFrases)
    ss = []
    ss.append(mediaPalavras)
    ss.append(typeToken)
    ss.append(hapax)
    ss.append(mediaSentecas)
    ss.append(complx)
    ss.append(mediaFrases)
    #print(ss)
    return ss
def avalia_textos(textos, ass_cp):
    i = 0
    ai = False
    anterior = False
    ss = 0
    while len(textos) > i:
        #print(i)
        texto = textos[i]
        ss = calcula_assinatura(texto)
        #print('1:', ss)
        cp = compara_assinatura(ass_cp, ss)
        #print('2:', cp)
        if not anterior or anterior > cp:
            anterior = cp
            ai = i
        i += 1
    return ai + 1
def chngcarac (texto):
    carac = ['"', "'", '.', '(', ')', ';', ',', ':']
    i = 0
    c = 0
    while c < len(carac):
        out = ''
        while i < len(texto):
            if texto[i] != carac[c]:
                out = out + texto[i]
            else:
                out = out + ' '
            i += 1
        c += 1
        i = 0
        texto = out
    return out
def main():
    textos = le_textos()
    ass_cp = le_assinatura()
    ai = avalia_textos(textos, ass_cp)
    print('O autor do texto', ai, 'está infectado com COH-PIAH')
main()
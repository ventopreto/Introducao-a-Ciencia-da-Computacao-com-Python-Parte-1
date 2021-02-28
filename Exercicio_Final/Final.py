import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser
    comparada com os textos fornecidos"""
    ''' 
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    '''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = 4.51
    ttr = 0.693
    hlr = 0.55
    sal = 70.82
    sac = 1.82
    pal = 38.5
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""

    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
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
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def gerar_lista_frases(frase):
    return separa_palavras(frase)


def relacao_type_token(lista_frase):
    return n_palavras_diferentes(lista_frase) / n_total_palavras(lista_frase)



"""Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de 
sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença). """


def gerar_lista_sentenca(texto):
    return separa_sentencas(texto)


def tamanho_medio_sentenca(lista_sentenca):
    x = 0
    for sentenca in lista_sentenca:
        if "." in sentenca:
            x += len(sentenca) - 1
        else:
            x += len(sentenca)
    return x / len(lista_sentenca)


"""Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por 
exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que 
aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale  3 / 5 = 0.6 """


def hapax(lista_frase):
    return n_palavras_unicas(lista_frase) / n_total_palavras(lista_frase)


'''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os 
caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase). '''


def tamanho_medio_frase(lista_sentenca):
    total_frase = 0
    lista = []
    x = 0
    # criando uma lista de frases
    for sentenca in lista_sentenca:
        lista.append(separa_frases(sentenca))
    # o primeiro for serve pra iterar as frases que são listas
    for lista_frase in lista:
        # o segundo for serve pra buscar os caracteres totais de cada frase
        for item in lista_frase:
            x += (len(item))
        total_frase += (len(lista_frase))
    return x / total_frase

'''
    Complexidade de sentença é o número total de frases divido pelo número de sentenças.
'''


def n_total_frases(lista_sentenca):
    lista = []
    total_frase = 0
    for sentenca in lista_sentenca:
        lista.append(separa_frases(sentenca))
    for frase in lista:
        total_frase += len(frase)
    return total_frase


def tamanho_medio_palavra(lista_palavra):
    return soma_tamanho_palavra(lista_palavra) / n_total_palavras(lista_palavra)


def soma_tamanho_palavra(lista_palavra):
    x = 0
    for palavra in lista_palavra:
        x += len(palavra)
    return x


def n_total_palavras(lista_palavras):
    return len(lista_palavras)

def gerar_lista_palavras(texto):
    lista_palavras = []
    for palavra in separa_palavras(texto):
        palavra = palavra.replace("," , "").replace("." , "").replace("?" , "").replace("!" , "").replace(":" , "").replace(";" , "")
        lista_palavras.append(palavra)
    return lista_palavras



def compara_assinatura(as_a, as_b):
    """IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas
    assinaturas. """
    sab = 0
    for i in range(len(as_a)):
        sab += abs(as_a[i] - as_b[i])
    return sab/6
    pass


def calcula_assinatura(texto):
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto."""
    wal = (tamanho_medio_palavra(gerar_lista_palavras(texto)))
    ttr = (relacao_type_token(gerar_lista_palavras(texto)))
    hlr = hapax(gerar_lista_palavras(texto))
    sal = (tamanho_medio_sentenca(gerar_lista_sentenca(texto)))
    sac = n_total_frases(gerar_lista_sentenca(texto)) / len(gerar_lista_sentenca(texto))
    pal = (tamanho_medio_frase(gerar_lista_sentenca(texto)))
    return [wal, ttr, hlr, sal, sac, pal]
    pass


def avalia_textos(textos, ass_cp):
    """IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH. """
    copia = 1000000
    index_copia = 1000000
    for index, texto in enumerate(textos, start=1):
        atual = compara_assinatura(calcula_assinatura(texto), ass_cp)
        if atual < copia:
            copia = atual
            index_copia = index
    print(f"O autor do texto {index_copia} está infectado com COH-PIAH")
    return index_copia
    pass

texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

avalia_textos(le_textos(),le_assinatura())




"""a = (compara_assinatura(calcula_assinatura(l[0]), le_assinatura()))
print(a)
b = (compara_assinatura(calcula_assinatura(l[1]), le_assinatura()))
print(b)
if a < b:
    print("A Sofre de Copia")
else:
    print("B Sofre de Copia")"""

"""Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, 
na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, 
gato, caçava, rato). Nessa frase, a relação Type-Token vale  4/5 = 0.8 frase("o, gato, caçava, rato") """
frase = "o, gato, caçava, o, rato"




'''




>calcula_assinatura(texto)
>[4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]'''

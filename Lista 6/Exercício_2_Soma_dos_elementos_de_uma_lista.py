'''
Exercício 2 - Soma dos elementos de uma lista
Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
'''

def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma+= item
    return soma





lista = [2, 4, 2, 2, 3, 3, 1,3]
print(soma_elementos(lista))
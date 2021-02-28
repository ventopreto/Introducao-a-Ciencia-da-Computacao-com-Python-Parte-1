'''
Exercício 1 - Maior elemento de uma lista
Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
'''

def maior_elemento(lista):
    maior = lista[0]
    for item in lista:
        if maior < item:
            maior = item
    return maior

lista = [2, 4, 2, 2, 3, 3, 1,3,5]
maior_elemento(lista)
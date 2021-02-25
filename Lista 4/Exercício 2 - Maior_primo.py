'''Escreva a função maior_primo que recebe um número inteiro maior ou
igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função'''
def primo(n):
    i = 2
    divisor = i
    nprimo = True
    while i < 1000:
        resto = n % i
        divisor = n // i
        i += 1
        if (divisor > 1 and resto == 0):
            nprimo = False
            break
    return nprimo

'''Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o 
número dado checando se o número é primo ou não; se for, guarde numa variável. 
Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.'''


def maior_primo(n):
    i = 0
    while i <= n:
        if primo(i):
            maiorprimo = i
        i+=1
    return maiorprimo

print(primo(2))
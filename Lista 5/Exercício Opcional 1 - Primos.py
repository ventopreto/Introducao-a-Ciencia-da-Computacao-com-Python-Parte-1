'''
Exercício 1 - Primos
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a 
quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
'''''

def primo(n):
    i = 2
    divisao = n // i
    resto = n % i
    eprimo = False
    while i <= n:
        divisao = n // i
        resto = n % i
        eprimo = False
        if resto == 0:
            if divisao == 1:
                eprimo = True
                break
            else:
                break
        else:
            i+=1
    return eprimo



def n_primos(n):
    i = 2
    count = 0
    while i <= n:
        if primo(i):
            count+=1
            i+=1
        else:
            i+=1
    return count

n = int(input("digite n: "))
print(n_primos(n))
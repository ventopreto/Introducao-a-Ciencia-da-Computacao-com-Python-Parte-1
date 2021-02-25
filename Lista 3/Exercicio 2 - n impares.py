'''Exercício 2
Receba um número inteiro positivo na entrada e imprima os n
primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.'''

n = int(input("Digite um numero: "))
i = 1

while i // n != 2:
    if i % 2 == 0:
        i+=1
    else:
        print(i)
        i+=1

'''Exercício 1
Escreva um programa que receba um número natural  n na entrada e imprima  n! (fatorial) na saída.'''
n = int(input("Digite um numero: "))
fatorial = n
while n > 2:
    fatorial = fatorial * (n - 1)
    n-= 1
if n == 0:
    print(1)
else:
    print(fatorial)



'''Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima

 par

quando o número for par ou

ímpar

quando o número for ímpar.'''

num = int(input("Digite um numero: "))
if num % 2 == 0:
    print("par")
else:
    print("ímpar")

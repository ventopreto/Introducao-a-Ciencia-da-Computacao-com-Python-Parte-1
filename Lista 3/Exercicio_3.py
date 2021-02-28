"""Exercício 3
  Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída"""

num = input("Digite um numero :")

tamanho = len(num)
num = int(num)
i = 0
soma = 0
while i < tamanho:
    soma+=(num % (10**(tamanho-(i))) // (10**(tamanho-(i+1)))  )
    i+=1
print(soma)

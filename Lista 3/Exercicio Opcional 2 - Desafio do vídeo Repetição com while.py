'''Exercício 2 - Desafio do vídeo "Repetição com while"
Escreva um programa que receba um número inteiro na entrada e verifique se o
número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
Caso exista, imprima "sim"; se não existir, imprima "não".'''

n = input("Digite um numero: ")
x = len(n)
e = 10**(x)
n = int(n)
resultado = -10000000000000000
repetido = False
anterior = -10000000000000000
while 0 < x:
    resultado = n % 10**x // 10**(x-1)
    if resultado == anterior:
        repetido = True
    anterior = resultado
    x-=1
if repetido:
    print("sim")
else:
    print("não")
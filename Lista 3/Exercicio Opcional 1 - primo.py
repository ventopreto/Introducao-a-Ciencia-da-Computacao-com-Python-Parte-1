''' Escreva um programa que receba um número inteiro positivo na entrada e
verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".'''

n = int(input("Digite um numero: "))
if n < 10:
    if (n / 2 == 1 or n / 3 == 1 or n / 5 == 1 or n / 7 == 1):
        print("primo")
    else:
        print("não primo")
elif not(n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        print("primo bla")
else:
    print("não primo")
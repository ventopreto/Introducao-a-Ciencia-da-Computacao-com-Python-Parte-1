'''Exercício 2 - Máximo com 3 parâmetros
Reescreva a função 'maximo' do outro exercício,
que devolve o maior valor dentre dois inteiros recebidos,
para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.'''

def maior(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def maximo(n1,n2,n3):
    if maior(n1,n2) > maior(n1,n3):
        return maior(n1,n2)
    else:
        return maior(n1,n3)


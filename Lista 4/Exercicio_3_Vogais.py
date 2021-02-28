'''Exercício 3 - Vogais
Escreva a função vogal que recebe um único caractere como parâmetro e devolve T
rue se ele for uma vogal e False se for uma consoante.'''


def vogal(entrada):
    entrada = entrada.lower()
    if entrada == "a" or entrada == "e" or entrada == "i" or entrada == "o" or entrada == "u":
        return True
    else:
        return False

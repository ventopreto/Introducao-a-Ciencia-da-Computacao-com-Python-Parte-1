'''Uma função computador_escolhe_jogada que recebe, como parâmetros,
os números n e m descritos acima e devolve um inteiro correspondente à
próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro)
de acordo com a estratégia vencedora.'''


'''Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e
verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo;
caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.'''

'''
Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e
inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores).
A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente.
A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja,
quantas peças foram removidas na última jogada e quantas restam na mesa.
Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou
 "Você ganhou!" conforme o caso.'''
def computador_escolhe_jogada(n, m):
    i=1
    while i <= m:
        if n % (n - i) == (n % m+1):
            pass
        else:
            print(f"{(n - i) == (n % m+1)}")
            print(f"{n-i, (n % m+1) }")
            print("não")
            i+=1
        print(n % m + 1)
        n -= i
        print(f"O computador removeu {i} peça, sobraram {n}")
        if n > 0:
            usuario_escolhe_jogada(n, m)
        else:
            print("A maquina venceu")

    else:
        n -= m
        print(n, (m + 1), (n % m+1))
        print(f"O computador removeu {m} peça, sobraram {n}")
        if n > 0:
            usuario_escolhe_jogada(n, m)
        else:
            print("A maquina venceu")

def usuario_escolhe_jogada(n,m):
    x = m+1
    while x > m:
        x = int(input("Quantas peças você quer remover?"))
        if x > m:
            print(f"O numero maximo de peças que pode ser removido é {m}")
        else:
            n -=x
            print(f"Tudo certo, você removeu {x}, restam {n}")
            if n > 0:
                computador_escolhe_jogada(n, m)
            else:
                print("você venceu")



def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))


    if n % (m+1) != 0:
        print("Computador começa!")
        computador_escolhe_jogada(n, m)
    else:
        print("Você começa!")
        usuario_escolhe_jogada(n, m)




partida()



'''
def computador_escolhe_jogada(n,m):
    i = 1
    print(f"printando {i}")
    while i <= m:
        print(f"Condição de vitoria? {(n - i) % (m + 1) == 0}")
        if(n - i) % (m+1) == 0:
            n-=i
            print(f"O computador removeu {i} peça, sobram {n}")
            break
        elif i == m and (n - m) != -1:
            print(f"{i == m and (n - m) != -1}")
            n -= m
            print(f"O computador removeu  {m} sobram {n}")
        else:
            i += 1

    if n > 0:
        print(f"printando n:{n}")
        usuario_escolhe_jogada(n, m)
    elif n <= 0:
        print("A maquina Venceu")

def usuario_escolhe_jogada(n,m):
    x = m+1
    while x > m:
        x = int(input("Quantas peças você quer remover?"))
        if x > m:
            print(f"O numero maximo de peças que pode ser removido é {m}")
        else:
            n -=x
            print(f"Tudo certo, você removeu {x}, restam {n}")
            if n > 0:
                computador_escolhe_jogada(n,m)
            else:
                print("você venceu")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))


    if n % (m+1) != 0:
        print("Computador começa!")
        computador_escolhe_jogada(n, m)
    else:
        print("Você começa!")
        usuario_escolhe_jogada(n, m)
'''
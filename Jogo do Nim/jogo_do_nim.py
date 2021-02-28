'''        elif i == m and (n - m) != -1:
            print(f"o que é isso? {i == m and (n - m) != -1}")
            retirado = m'''
def computador_escolhe_jogada(n, m):
    i = 1
    retirado = -1
    while i <= m:
        print(f"Condição de vitoria? {(n - i) % (m + 1) == 0}\n")
        if(n - i) % (m+1) == 0:
            retirado = i
            break
        elif print(f"Condição de vitoria? {(n - i) % (m + 1) != 0}\n"):
            retirado = m
        else:
            i += 1
    return retirado

def usuario_escolhe_jogada(n, m):
    x = m+1
    valido = False
    while valido == False:
        x = int(input("Quantas peças você vai tirar?\n"))
        if x > m or x <= 0:
            print(f"Oops! Jogada inválida! Tente de novo.\n")
        else:
            valido = True
            return x


def partida():
    j = 1
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? \n"))


    pcwin = 0
    youwin = 0

    if n % (m+1) != 0:
        print("Computador começa!\n")
        while n > 0:
            x = computador_escolhe_jogada(n, m)
            n -= x
            print(f"O computador tirou {x} peça.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                pcwin += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro. \n")

            x = usuario_escolhe_jogada(n, m)
            n -= x
            print(f"Você tirou {x} peça.")
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                youwin += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro. \n")

    else:
        print("Você começa!\n")
        while n > 0:
            x = usuario_escolhe_jogada(n, m)
            n -= x
            print(f"Você tirou {x} peça.")
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                youwin += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro. \n")

            x = computador_escolhe_jogada(n, m)
            n -= x
            print(f"O computador tirou {x} peça.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                pcwin += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro. \n")
    return youwin, pcwin
'''    elif n % (m+1) == 0:
        
        usuario_escolhe_jogada(n, m)
        while n > 0:
            j+=1
            print(f"**** Rodada {j} ****")
            computador_escolhe_jogada(n, m)
            usuario_escolhe_jogada(n, m)
'''

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2 \n")
num = int(input())
if num == 1:
    print("Voce escolheu um partida! \n")
    partida()
else:
    pcwin = 0
    youwin = 0
    j = 1
    print("Voce escolheu um campeonato! \n")
    print(f"**** Rodada {j} ****\n")
    partida()
    pcwin+=1
    j+= 1
    print(f"**** Rodada {j} ****\n")
    partida()
    pcwin += 1
    j += 1
    print(f"**** Rodada {j} ****\n")
    partida()
    pcwin += 1
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {youwin} X {pcwin} Computador")

'''
digite a largura: 10
digite a altura: 3
##########
##########
##########
'''

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
n = 0
i = 0
while i < a:
    n = 0
    while n < l:
        print("", end = '#')
        n+=1
    i+=1
    print()

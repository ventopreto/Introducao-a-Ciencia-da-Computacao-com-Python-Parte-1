import math
def main():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    imprime_raizes(a,b,c)

def delta(a,b,c):
    return (b ** 2) - (4 * a * c)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if d < 0:
        print("esta equação não possui raízes reais")
    elif d == 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        print(f"a raiz desta equação é {x1}")
    else:
        x1 = ((-b + math.sqrt(d)) / (2*a))
        x2 = ((-b - math.sqrt(d)) / (2*a))
        if x1 < x2:
            print(f"as raízes da equação são {x1} e {x2}")
        else:
            print(f"as raízes da equação são {x2} e {x1}")

main()

'''print(delta(2,12,-14))'''
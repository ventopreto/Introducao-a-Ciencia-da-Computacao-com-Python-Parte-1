valor = int(input("Digite um número inteiro"))
centena_de_milhar = valor // 10000
milhar = valor % 10000 // 1000
centena = valor % 1000 // 100
dezena = valor % 100 // 10
unidade = valor % 10
print(f" O dígito das dezenas é {dezena}")
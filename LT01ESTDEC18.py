n1 = 0
n2 = 0
diferenca = 0

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
if n1 < n2:
    diferenca = n2 - n1
    print("O resultado da diferença do maior pelo menor valor é: ", diferenca)
else:
    diferenca = n1 - n2
    print("O resultado da diferença do maior pelo menor valor é: ", diferenca)
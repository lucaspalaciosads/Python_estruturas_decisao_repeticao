#44. Receba o número da base e do expoente. Calcule e mostre o valor da potência.
base = 0
expoente = 0
resultado = 0

base = float(input("Digite o número da base: "))
expoente = float(input("Digite o número do expoente: "))
resultado = base ** expoente
print(f"O valor da potência é: {resultado}")
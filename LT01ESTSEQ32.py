N = 0
Fatorial = 0
Nmenor = 0

N = int(input("Digite o número: "))
Fatorial = 1
Nmenor = N
while Nmenor >= 1:
    Fatorial = (Fatorial * Nmenor)
    Nmenor = (Nmenor - 1)
print("O fatorial de ", N, "é: ", Fatorial)
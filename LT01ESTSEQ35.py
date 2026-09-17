#35. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
N1 = 0
N2 = 0
Maior = 0
Menor = 0
Soma = 0
N = 0

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
if N1 > N2:
    Maior = N1
    Menor = N2
else:
    Maior = N2
    Menor = N1
Soma = 0
N = Menor
while N <= Maior:
    if N % 2 != 0:
        Soma = Soma + N
    N = N + 1
print("O resultado é: ", Soma)
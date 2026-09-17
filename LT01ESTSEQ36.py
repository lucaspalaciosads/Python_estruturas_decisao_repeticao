N = 0
Soma = 0
Fatorial = 0
Termo = 0
I = 0

N = int(input("Digite um número inteiro N: "))
Soma = 1.0
Fatorial = 1
for I in range(1, N + 1):
    Fatorial *= I
    Termo = 1 / Fatorial
    Soma += Termo
    print(f"Termo {I}: 1 / {I}! = {Termo:.2f}")
print(f"\nValor total da série = {N}: {Soma:.2f}")
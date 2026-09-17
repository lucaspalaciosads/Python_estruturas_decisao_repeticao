#42. Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
Soma = 0
Denominador = 0
Numerador = 0
Termos = 0
Serie = 0

Soma = 0
Denominador = 1
Termos = []
for Numerador in range(1, 51):
    Termos.append(f"{Numerador}/{Denominador}")
    Soma += Numerador / Denominador
    Denominador += 2
Serie = " + ".join(Termos)
print("Série: ")
print(Serie)
print("-" * 50)
print(f"O resultado da série é: {Soma:.2f}")
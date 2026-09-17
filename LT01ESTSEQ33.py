#Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
N = 0.0
Soma = 0.0
Cont = 0.0
Serie = 0.0

N = int(input("Digite um número: "))
Soma = 0.0
Cont = 1
Serie = ""
while Cont <= N:
    Soma += 1 / Cont
    if Cont == 1:
        Serie += "1"
    else:
        Serie += f" + 1/{Cont}"
    Cont += 1
print(f"\nSérie: {Serie}")
print(f"Soma total: {Soma:.4f}")
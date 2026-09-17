#40. Verifique e mostre todos os números primos existentes entre eles.
N1 = 0
N2 = 0
Menor = 0
Maior = 0
Cont = 0
Primos = 0
Teste = 0

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o primeiro número: "))
if N1 > N2:
    Maior = N1
    Menor = N2
else:
    Maior = N2
    Menor = N1
print(f"Números primos entre {Menor} e {Maior}:")
for Cont in range(Menor, Maior + 1):
    if Cont > 1:
        Primos = True
        for Teste in range(2, int(Cont**0.5) + 1):
            if Cont % Teste == 0:
                Primos = False
                break
        if Primos:
            print(Cont, end=" ")

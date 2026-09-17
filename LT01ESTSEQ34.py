#34.Calcule e mostre os resultados da tabuada desse número.
N = 0
Cont = 0
Tab = 0

N = int(input("Digite um número: "))
print(f"\nA tabuada de {N} é: ")
for Cont in range (1, 11):
    Tab = N * Cont
    print(f"{N} x {Cont} = {Tab}")
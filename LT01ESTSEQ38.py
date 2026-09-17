N1 = 0
N2 = 0
N = 0
Cont = 0

while Cont <= 5:
    N = int(input("Digite um número inteiro de 0 a 100 (somente positivo): "))
    if N <= 0:
        print("Valor inválido. Escreva apenas números positivos!")
    if N > N1:
        N1 = N
    if N < N2:
        N2 = N
    Cont += 1
print(f"O maior valor digitado foi: {N1}")
print(f"O menor valor digitado foi: {N2}")
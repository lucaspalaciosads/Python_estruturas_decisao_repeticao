#37. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
N = 0
A = 0
B = 0
Fibonacci = 0
Cont = 0

N = int(input("Digite um número: "))
A = 1
B = 1
Cont = 0
if N <= 0:
    print("Digite um número inteiro maior que 0")
elif N == 1:
    print(f"O cálculo de Fibonacci é {A}")
else:
    while Cont <= N:
        print(A, end=" - " if Cont < N - 1 else "\n")
        Fibonacci = A + B
        A = B
        B = Fibonacci
        Cont += 1
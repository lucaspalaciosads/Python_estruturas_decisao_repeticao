N = 0

N = int(input("Digite o valor: "))
if N / 2 == N // 2 and N / 3 == N // 3:
    print("O número é divisível por 2 e 3")
elif N / 2 == N // 2:
    print("O número é divisível por 2")
elif N / 3 == N // 3:
    print("O número é divisível por 3")
else:
    print("O número não é divisível por 2, nem por 3")
N1 = 0
N2 = 0

N1 = int(input("Digite o primeiro valor: "))
N2 = int(input("Digite o segundo valor: "))
if N1 < N2:
    if N2 / N1 == N2 // N1:
        print("O número {} é divisível por {}".format(N2, N1))
    else:
        print("O número {} não é divisível por {}".format(N2, N1))
elif N1 > N2:
    if N1 / N2 == N1 // N2:
        print("O número {} é divisível por {}".format(N1, N2))
    else:
        print("O número {} não é divisível por {}".format(N1, N2))
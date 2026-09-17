Tinv = 0.0
Vinv = 0.0
Result = 0.0

Vinv = float(input("Digite o valor do investimento: R$ "))
Tinv = float(input("Digite o tipo de investimento (1 - poupança, 2 - renda fixa): "))
if Tinv == 1:
    Result = Vinv * 1.03
    print("O valor corrigido em 30 dias: R$ ", Result)
elif Tinv == 2:
    Result = Vinv * 1.05
    print("O valor corrigido em 30 dias: ", Result)
else:
    print("Tipo de investimento inválido.")
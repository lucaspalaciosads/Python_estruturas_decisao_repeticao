PA = 0.0
VM = 0.0
NV = 0.0

VM = float(input("Digite a média mensal de vendas: "))
PA = float(input("Digite o preço do produto: R$ "))
if VM < 500 and PA < 30:
    NV = PA * 1.10
    print("O novo preço do produto é: R$ ", NV)
elif VM >= 500 and VM < 1000 and PA >= 30 and PA < 80:
    NV = PA * 1.15
    print("O novo preço do produto é: R$ ", NV)
elif VM >= 1000 and PA >= 80:
    NV = PA * 0.95
    print("O novo preço do produto é: R$ ", NV)
else:
    NV = PA
    print("O preço do produto permanecerá: R$ ", NV)
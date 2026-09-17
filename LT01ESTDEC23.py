V1 = 0.0
V2 = 0.0
V3 = 0.0
V4 = 0.0

V1 = float(input("Digite o primeiro valor: "))
V2 = float(input("Digite o segundo valor: "))
V3 = float(input("Digite o terceiro valor: "))
V4 = float(input("Digite o quarto valor: "))
if V4 <= V1:
    print(V4, ", ", V1, ", ", V2, ", ", V3)
elif V4 > V1 and V4 <= V2:
    print(V1, ", ", V4, ", ", V2, ", ", V3)
elif V4 > V2 and V4 <= V3:
    print(V1, ", ", V2, ", ", V4, ", ", V3)
else:
    print(V1, ", ", V2, ", ", V3, ", ", V4)
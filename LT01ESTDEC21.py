N1 = 0.0
N2 = 0.0
N3 = 0.0
N4 = 0.0
Media = 0.0

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))
Media = (N1 + N2 + N3 + N4) / 4
print("A média das notas é:", Media)
if Media >= 6:
    print("Aprovado")
elif Media >= 3:
    print("Exame")
else:
    print("Retido")
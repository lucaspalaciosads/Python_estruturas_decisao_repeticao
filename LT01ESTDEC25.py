HI = 0
HF = 0
MI = 0
MF = 0
H = 0
T = 0
R = 0

HI = int(input("Digite a hora inicial: "))
MI = int(input("Digite o minuto inicial: "))
HF = int(input("Digite a hora final: "))
MF = int(input("Digite o minuto final: "))
T = (HF * 60 + MF) - (HI * 60 + MI)
if T < 0:
    T = T + 1440
H = T // 60
R = T % 60
print("O tempo total é de", H, "hora(s) e", R, "minuto(s)")
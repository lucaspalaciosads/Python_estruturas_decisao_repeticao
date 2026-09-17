NV = 0
EC = 0
TD = 0
DS = 0
DT = 0
Cont = 0

NV = int(input("Digite o número de voltas: "))
EC = int(input("Digite a extensão do circuito (em metros): "))
TD = int(input("Digite o tempo de duração (em minutos): "))

DS = NV * EC / 1000
DT = TD / 60
Cont = DS / DT
print("A velocidade média do carro é de: ", Cont, "Km/h")
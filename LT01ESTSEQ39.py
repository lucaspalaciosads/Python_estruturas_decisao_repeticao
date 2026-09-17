#39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
#Casa: 1 2 3 4 ... 64
#Qdte: 1 2 4 8 ... N
Casa = 0
Quantidade = 0
Calculo = 0

Quantidade = 1
Calculo = 1
print("Casa ","grãos")
print(Quantidade, Calculo)
for Casa in range (1, 64):
    Calculo = Quantidade * 2
    Quantidade = Calculo
    Casa += 1
    print(Casa, Calculo)
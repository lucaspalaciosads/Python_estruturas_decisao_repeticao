#Mostre as possib. de 2 dados a soma tenha como resultado 7.
Dado1 = 0
Dado2 = 0
Calc = 0
Combinacao = 0

Calc = []
for Dado1 in range (1, 7):
    for Dado2 in range (1, 7):
        if Dado1 + Dado2 == 7:
            Calc.append ((Dado1, Dado2))
print("As possibilidades de obter soma 7 são:")
for Combinacao in Calc:
    print(f"Dado 1: {Combinacao[0]} | Dado 2: {Combinacao[1]}")
print(f"\nTotal de possibilidades: {len(Calc)}")
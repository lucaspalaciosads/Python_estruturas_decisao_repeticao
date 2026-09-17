#45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 - ... + 15/225
soma_total = 0.0
termos_texto = []

for n in range(1, 16):
    numerador = n
    denominador = n ** 2
    valor_termo = numerador / denominador
    if n % 2 == 0:
        soma_total -= valor_termo
        termos_texto.append(f"- {numerador}/{denominador}")
    else:
        soma_total += valor_termo
        if n == 1:
            termos_texto.append(f"{numerador}")
        else:
            termos_texto.append(f"+ {numerador}/{denominador}")
serie_completa = " ".join(termos_texto)
print("Série gerada:")
print(serie_completa)
print(f"\nResultado da soma: {soma_total:.5f}")
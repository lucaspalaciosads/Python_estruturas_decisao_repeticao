altura_ana = 110
altura_maria = 150
anos = 0

while altura_ana <= altura_maria:
    altura_ana += 3
    altura_maria += 2
    anos += 1
print(f"Serão necessários {anos} anos para Ana ser maior que Maria.")
print(f"Altura final de Ana: {altura_ana / 100:.2f} m")
print(f"Altura final de Maria: {altura_maria / 100:.2f} m")
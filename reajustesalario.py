salario = float(input())
salario_minino = float(input())

if salario <= salario_minino * 3:
    novo = salario + (salario * 20 / 100)
elif salario > salario_minino * 3 and salario <= salario_minino * 5:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)


if novo < salario_minino * 1.5:
    novo = salario_minino * 1.5
elif novo > salario_minino * 20:
    novo = salario_minino * 20

print(f"{novo:.2f}")

horas_trabalhadas = (int(input()))
horas_extras = (int(input()))

salario_base = 2500.00
valor_hora = salario_base / 200

salario_horas = salario_base

if horas_trabalhadas < 200:
    salario_horas = horas_trabalhadas * valor_hora

salarios_horas_extras = 0
if horas_extras > 0:
    salarios_horas_extras = round((horas_extras * valor_hora) + (horas_extras * valor_hora) * 20 / 100, 2)

salario_bruto = salario_horas + salarios_horas_extras
imposto = round(salario_bruto * 13 / 100, 2)
social = round(salario_bruto * 9 / 100, 2)
salario_liquido = salario_bruto - imposto - social

print(f"- Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (13%) : R$ {imposto:.2f}")
print(f"- INSS (9%) : R$ {social:.2f}")
print(f"- Salário Líquido : R$ {salario_liquido:.2f}")

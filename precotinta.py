area = int(input())

galao_litros = 3.6
cobertura_litros = 18
preco_galao = 25.00

metros_galao = cobertura_litros * galao_litros
galoes = max([round(area / metros_galao), 1])
valor = galoes * preco_galao

print(f"- área de cobertura: {area}")
print(f"- número de galões: {galoes}")
print(f"- valor a ser pago: R$ {valor:.2f}")
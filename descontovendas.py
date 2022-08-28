valor_compra = float(input())

valor_com_desconto = valor_compra - (valor_compra * 20 / 100)

if valor_compra > 1000:
    valor_com_desconto -= (valor_compra - 1000) * 15 / 100
if valor_compra >= 500:
    valor_com_desconto -= (valor_compra * 10 / 100)

print(f"{valor_com_desconto:.1f}")

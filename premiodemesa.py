comprimento_mesa = float(input())
largura_da_mesa = float(input())
numero_de_gavetas = int(input())
tipo_de_madeira = input()

valor_gaveta = 30
if numero_de_gavetas > 0:
    valor_gaveta *= numero_de_gavetas
else:
    valor_gaveta = 0

valor_metro_quadrado = (comprimento_mesa * largura_da_mesa * 100) + valor_gaveta

valor_total_mesa = valor_metro_quadrado
if tipo_de_madeira == "mogno":
    valor_total_mesa += 150
elif tipo_de_madeira == "carvalho":
    valor_total_mesa += 125
if largura_da_mesa > 2:
    valor_total_mesa += 50
if valor_total_mesa < 200:
    valor_total_mesa = 200

print(f"{valor_total_mesa:.1f}")


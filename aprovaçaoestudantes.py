nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())

peso_1 = float(input())
peso_2 = float(input())
peso_3 = float(input())

media = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3)

print(media >= 6)
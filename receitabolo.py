a, b, c = [int(w) for w in input().split()]

divi_trigo = int(a / 2)
divi_ovos = int(b / 3)
divi_leite = int(c / 5)

menor = divi_trigo
if divi_ovos < menor:
    menor = divi_ovos
if divi_leite < menor:
    menor = divi_leite

print(menor)



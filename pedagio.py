l, d = [int(w) for w in input().split()]
k, p = [int(w) for w in input().split()]

pedagios = round(l / d)
valor_pedagio = round(pedagios * p)
valor_km = round(l * k)
gasto = round(valor_pedagio + valor_km)

gasto = int(gasto)

print(f"{gasto}")
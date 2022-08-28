capital = float(input())
meses = float(input())
taxa = float(input())

montante = round(capital * (1 + (taxa / 100)) ** meses, 2)
print(f"montante : {montante:.2f}")


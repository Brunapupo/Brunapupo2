#cogido em cosntrução
a, b, c = [int(w) for w in input().split()]
x, y, z = [int(w) for w in input().split()]

volume_conteiner = a * b * c
volume_navio = x * y * z
quantidade_conteiners = volume_navio // volume_conteiner


if c > z:
    quantidade_conteiners = 0

print(f"{quantidade_conteiners}")


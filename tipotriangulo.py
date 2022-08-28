lado1 = abs(float(input()))
lado2 = abs(float(input()))
lado3 = abs(float(input()))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("equilátero")
    elif lado1 != lado2 != lado3 != lado1:
        print("escaleno")
    else:
        print("isósceles")


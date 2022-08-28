import math

nota = float(input())

parte_inteira = math.floor(nota)

valor_casa_decimal = round(nota - int(nota), 5)

if(valor_casa_decimal >= 0 and valor_casa_decimal < 0.25):
    print(f"{parte_inteira:.1f}")
elif(valor_casa_decimal >= 0.25 and valor_casa_decimal < 0.75):
    print(f"{parte_inteira+0.5:.1f}")
elif(valor_casa_decimal >= 0.75 and valor_casa_decimal < 1.0):
    print(f"{parte_inteira+1.0:.1f}")

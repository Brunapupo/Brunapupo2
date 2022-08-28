sistema_de_entrada = input()
temperatura = float(input())
sistema_de_saida = input()

temperatura_convertida = temperatura

#Celsius
if sistema_de_entrada == "c" and sistema_de_saida == "f":
     temperatura_convertida = (temperatura * 9/5) + 32
elif sistema_de_entrada == "c" and sistema_de_saida == "k":
     temperatura_convertida = (temperatura + 273.15)
elif sistema_de_entrada == "c" and sistema_de_saida == "r":
     temperatura_convertida = (temperatura * 9/5 + 491.67)

# Fahrenheit
if sistema_de_entrada == "f" and sistema_de_saida == "c":
     temperatura_convertida = (temperatura - 32) * 5/9
elif sistema_de_entrada == "f" and sistema_de_saida == "k":
     temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
elif sistema_de_entrada == "f" and sistema_de_saida == "r":
     temperatura_convertida = (temperatura * 9/5 + 491.67)


# Kelvin
if sistema_de_entrada == "k" and sistema_de_saida == "c":
     temperatura_convertida = (temperatura - 273.15)
elif sistema_de_entrada == "k" and sistema_de_saida == "f":
     temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
elif sistema_de_entrada == "k" and sistema_de_saida == "r":
     temperatura_convertida = (temperatura * 1.8)


# rankine
if sistema_de_entrada == "r" and sistema_de_saida == "c":
     temperatura_convertida = (temperatura - 491.67) * 5/9
elif sistema_de_entrada == "r" and sistema_de_saida == "f":
     temperatura_convertida = (temperatura - 459.67)
elif sistema_de_entrada == "r" and sistema_de_saida == "k":
     temperatura_convertida = (temperatura * 5/9)

print(f"{temperatura_convertida:.5f}")




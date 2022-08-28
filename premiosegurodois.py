valor_veiculo = float(input())
sexo = input()
idade_seguro = int(input())


#Valor veiculo
valor_seguro = valor_veiculo * 10/100

valor_desconto = 0.0
#calculo Masculino
if sexo == "M" and 25 <= idade_seguro < 33:
    valor_desconto = valor_seguro * 10/100
elif sexo == "M" and idade_seguro >= 33:
    valor_desconto = valor_seguro * 20/100
#Calculo feminino
if sexo == "F" and idade_seguro <= 24:
    valor_desconto = valor_seguro * 5/100
elif sexo == "F" and 25 <= idade_seguro <= 33:
    valor_desconto = valor_seguro * 20/100
elif sexo == "F" and idade_seguro > 33:
    valor_desconto = valor_seguro * 35/100

valor_seguro = valor_seguro - valor_desconto
print(f"{valor_seguro:.2f}")

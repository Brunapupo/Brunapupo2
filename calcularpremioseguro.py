valor_veiculo = float(input())
classe_desconto = input()
carro_nacionalidade = input()
idade_segurado = int(input())

valor_seguro = 0.0
#calculo Nacionalidade
if carro_nacionalidade == "nacional":
    valor_seguro = valor_veiculo * 10/100
elif carro_nacionalidade == "estrangeira":
    valor_seguro = valor_veiculo * 15/100

valor_do_desconto = 0.0
#desconto tabela
if classe_desconto == "A":
    valor_do_desconto = valor_seguro * 30/100
elif classe_desconto == "B":
    valor_do_desconto = valor_seguro * 20/100
elif classe_desconto == "C":
    valor_do_desconto = valor_seguro * 10/100
elif classe_desconto == "D":
    valor_do_desconto = valor_seguro * 5/100

#calculo idade
if idade_segurado > 24:
    valor_do_desconto = valor_do_desconto + valor_seguro * 10/100

print(f"{valor_seguro - valor_do_desconto:.2f}")

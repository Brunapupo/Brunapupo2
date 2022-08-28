idade = int(input())

anos = int(idade // 365)
saldo = idade - anos * 365

meses = int(saldo // 30)
dias = saldo - meses * 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
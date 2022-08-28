nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = ((nota1 + nota2 + nota3) / 3)

if(media >= 9.0):
    print("Ótimo")
elif(media >= 7.5 and media < 9.0):
    print("Bom")
elif(media >= 6.0 and media < 7.5):
    print("Satisfatório")
else:
    print("Insuficiente")

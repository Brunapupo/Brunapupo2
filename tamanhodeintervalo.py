primeiro_Numero = int(input())
ultimo_Numero = int(input())

if primeiro_Numero > ultimo_Numero:
    resultado = primeiro_Numero - ultimo_Numero + 1
else:
    resultado = ultimo_Numero - primeiro_Numero + 1

print(f"numero de elementos : {resultado}")

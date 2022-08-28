num_competidores, qtd_total_folhas, qtd_folhas_competidor = [int(w) for w in input().split()]

resultado = qtd_total_folhas // num_competidores < qtd_folhas_competidor

if resultado:
    print("N")
else:
    print("S")

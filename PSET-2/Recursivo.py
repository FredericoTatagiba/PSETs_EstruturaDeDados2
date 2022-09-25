n = int(input("Quantos discos tem a torre?\nResposta: "))


#  função para resolução da Torre
def MovimentosHanoi(n, origem, destino, aux):
    if n == 0:
        return
    # faz o movimento a partir da origem
    MovimentosHanoi(n - 1, origem, aux, destino)
    # printa o movimento feito
    print("Mover disco", n, "da torre", origem, "para a torre", destino)
    # faz o movimento a partir da auxiliar
    MovimentosHanoi(n - 1, aux, destino, origem)


MovimentosHanoi(n, 'origem', 'destino', 'auxiliar')
t_moves = pow(2, n) - 1

print(f"\n\nNumero de movimentos para resolver: {t_moves}")

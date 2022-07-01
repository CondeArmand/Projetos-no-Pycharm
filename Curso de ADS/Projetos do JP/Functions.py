def crie_matriz(n_linhas, n_colunas):
    """ (int, int) -> matriz (lista de listas)
Cria e retorna uma matriz com n_linhas linha e n_colunas
olunas em que cada elemento é igual ao valor dado.
"""

    matriz = []  # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = []  # lista vazia
        for j in range(n_colunas):
            linha.append(int(input(f'Informe um valor para {i}, {j}: ')))

        # coloque linha na matriz
        matriz.append(linha)

    return matriz


def linha():
    print('\n================================')


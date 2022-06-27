def decimalPraBinario(a=int):
    """

    :param a: Recebe um valor decimal inteiro
    :return: Retorna um valor binario já formatado
    """
    return bin(a)[2:]


def criaMatrizes(key=None):
    """

    :param key: Caso seja informado um valor True para ela, irá imprimir na tela a matriz criada
    :return: retorna uma matriz em forma de lista
    """
    from random import randint
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = randint(1, 50)
    if key is True:
        print('-=-' * 30)
        for l in range(0, 3):
            for c in range(0, 3):
                print(f'[{matriz[l][c]:^5}]', end='')
            print()
    return matriz


def somaMatrizes(a=list, b=list, key=None):
    """

    :param a: Recebe uma matriz (lista)
    :param b: Recebe uma matriz (lista)
    :param key: Caso seja informado um valor True, a função irá imprimir a matriz já formatada
    :return: retorna a soma de duas matrizes em forma de lista
    """
    s = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for line in range(0, 3):
        for cols in range(0, 3):
            s[line][cols] = a[line][cols] + b[line][cols]
    if key is True:
        print('-=-' * 30)
        for l in range(0, 3):
            for c in range(0, 3):
                print(f'[{s[l][c]:^5}]', end='')
            print()
    else:
        return s


arquivo = open('Documentação da prova.txt', 'a')
arquivo.write('''-As funções utilizadas na segunda questão estão presentes no arquivo "Functions" e todas contém 
docstrings para esclarecer seu funcionamento, basta usar o comando help().
A questão2B irá gerar matrizes 3x3 aleatórias para maior comodidade na hora de testar.
 ''')
arquivo.close()
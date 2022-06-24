from Functions import criaMatrizes, somaMatrizes
print('''          <<< Somador de Matrizes >>>
O programa irá gerar duas matrizes aleatorias e soma-lás''')
matriz1 = criaMatrizes()
matriz2 = criaMatrizes()
soma = somaMatrizes(matriz1, matriz2, key=True)
print(soma)
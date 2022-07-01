from Functions import crie_matriz, linha
import numpy as np
# Entrada de dados
n = int(input('Informe uma matriz quadrada válida: '))
linha()
matrizA = crie_matriz(n, n) # Cria uma matriz quadrada, com os valores indicados pelo usuário
linha()
matrizB = crie_matriz(n, n) # Cria uma matriz quadrada, com os valores indicados pelo usuário
linha()
# calculando...
matrizBT = np.transpose(matrizB) # gera a transposta da matriz B
x = np.trace(matrizA) # soma a diagonal principal da matriz A
matrizA = np.array(matrizA)
matrizXA = np.multiply(matrizA, x) # Multiplica a Matriz A com X
matrizR = np.matmul(matrizXA, matrizBT) # Calcula a resultante entre a operação anterior com a transposta da matriz B
print(matrizR)
linha()

lista = []  # lista estabelicida para ser usada durante o codigo

# for n para adicionar a quantidade de valores pedidos na lista
for n in range(15):
    num = int(input('Informe um valor: '))
    lista.append(num)

# essa parte serve para definir os indices escolhidos pelo usuario
indA = int(input('Informe o indice A: '))
indB = int(input('Informe o indice B: '))
lista = lista[indA:indB + 1]

# parte do final do codigo onde ele irá fazer a checagem de quais valores entre os indices escolhidos são impares.
for c in lista:
    if c % 2 != 0:
        print(c, end=' ')

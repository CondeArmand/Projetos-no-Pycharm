lista = []
qtad = int(input('Quantos números deseja inserir? '))
for c in range(qtad):
    lista.append(int(input('Infome um valor: ')))
print(f'Você digitou {qtad} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor 5', 'foi' if 5 in lista else 'não foi', 'encontrado na lista!')

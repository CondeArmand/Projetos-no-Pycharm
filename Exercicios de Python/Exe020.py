from random import shuffle
p1 = str(input('Primeiro nome: '))
p2 = str(input('Segundo nome: '))
p3 = str(input('Terceiro nome: '))
p4 = str(input('Quarto nome: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem de apresentação será:{}'.format(lista))

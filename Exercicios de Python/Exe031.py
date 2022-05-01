km = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(km * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(km * 0.45))
print('Tenha uma boa viagem!')

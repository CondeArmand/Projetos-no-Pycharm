nome = str(input('Qual é seu nome? ')).strip().capitalize()
if nome == 'Armando':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

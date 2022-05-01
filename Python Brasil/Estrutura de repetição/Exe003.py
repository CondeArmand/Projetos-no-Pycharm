while True:
    nome = input('Insira seu nome: ')
    idade = int(input('insira sua idade: '))
    salario = int(input('Informe seu salario: '))
    sexo = input('Informe seu sexo: ').lower()
    civil = input('Informe seu estado civil: ').lower()

    qtletras = nome.count('')
    sexos = ['m', 'f']
    civils = ['s', 'c', 'v', 'd']

    if qtletras > 3 and idade <= 150 and salario > 0 and sexo in sexos and civil in civils:
        print('Informações válidas')
        break
    else:
        print('Informações invalidas! Insira novamente!')


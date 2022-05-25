mais18 = homens = mulheresmenos20 = 0
sn = 'S'
sexo = ''
while sn == 'S':
    print('-' * 30)
    print(f'    CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    sn = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homem (ns) cadastrado (s)')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos')

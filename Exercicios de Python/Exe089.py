from time import sleep
temporary = list()
alunos = list()
SN_primary = SN_secondary = 's'
while SN_primary != -1:
    while SN_secondary == 's':
        temporary.append(input('Nome: '))
        temporary.append(float(input('Nota 1: ')))
        temporary.append(float(input('Nota 2: ')))
        alunos.append(temporary[:])
        temporary.clear()
        SN_secondary = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    print('-=-' * 40)
    print('No. NOME             MÉDIA')
    print('-' * 30)
    for i, l in enumerate(alunos):
        print(f'{i} {l[0]:^10} {(l[1] + l[2]) / 2:^20.1f}')
    print('-' * 30)

    while True:
        notas_alunos = int(input('Mostrar notas de qual aluno? (-1 Interrompe): '))
        if notas_alunos == -1:
            SN_primary = -1
            break
        else:
            print(f'Notas do {alunos[notas_alunos][0]} são {alunos[notas_alunos][1:]}')
            print('-' * 30)
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')

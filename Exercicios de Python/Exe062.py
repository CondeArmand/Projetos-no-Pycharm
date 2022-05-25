print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 10
total = 0
while cont != 0:
    for c in range(cont):
        print(f'{termo} -> ', end='')
        termo += razao
        total += 1
    print('PAUSA')
    cont = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

from datetime import date
ano_atual = date.today().year
maior_idades = 0
menor_idades = 0
for n in range(7):
    ano = int(input(f'Em que ano a {n + 1}ª pessoa nasceu? '))
    if ano_atual - ano >= 21:
        maior_idades += 1
    else:
        menor_idades += 1
print(f'ao todos tivemos 3 pessoas maiores de idade')
print(f'E também tivemos 4 pessoas menores de idade')

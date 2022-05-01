from datetime import date
idade = int(input('Insira seu ano de nascimento: '))
datual = date.today().year
dcheck = datual - idade
print('O Atleta tem {}'.format(dcheck))
if dcheck <= 9:
    print('Sua classificação é MIRIM.')
elif dcheck <= 14:
    print('Sua classificação é INFANTIL.')
elif dcheck <= 19:
    print('Sua classificação é JUNIOR.')
elif dcheck <= 25:
    print('Sua classificação é SÊNIOR.')
elif dcheck > 25:
    print('Sua classificação é MASTER.')

n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1 + n2) / 2
if media > 7:
    print('\033[4;32mSua media foi {}, você está aprovado!!!'.format(media))
elif media < 5:
    print('\033[4;31mSua media foi {}, você está reprovado!!!'.format(media))
else:
    print('\033[4;33mSua media foi {}, você está de recuperação!!!'.format(media))

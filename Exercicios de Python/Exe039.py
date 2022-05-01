from datetime import date
ano = int(input('Insira seu ano de nascimento: '))
data = date.today().year
idade = data - ano
if idade == 18:
    print('\033[4;32mJá está na hora de se alistar!!!')
elif idade < 18:
    print('\033[4;31mVocê ainda não tem a idade necessaria, seu alistamento será em {} anos'.format(18 - idade))
    print('\033[4;33mSeu alistamento será em {}.'.format((18 - idade) + data))
else:
    print('\033[4;31mVocê já deveria estar alistado faz {} anos!!!'.format(idade - 18))
    print('\033[4;33mSeu alistamento foi em {}.'.format(data - (idade - 18)))

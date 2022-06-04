from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] > 0:

    dados['Contratação'] = anodecontracao = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=-' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

dados = dict()
aluno = list()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input('Média: '))
if dados['Média'] >= 7:
    dados['Situacao'] = 'Aprovado'
else:
    dados['Situacao'] = 'Reprovado'
aluno.append(dados.copy())
for e in aluno:
    for k, v in e.items():
        print(f'{k} é igual a {v}')

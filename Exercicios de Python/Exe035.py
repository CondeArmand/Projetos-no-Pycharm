
ps = float(input('Informe o primeiro seguimento: '))
ss = float(input('Informe o segundo seguimento: '))
ts = float(input('Informe o terceiro segmento: '))
if ps < ss + ts and ss < ps + ts and ts < ps + ss:
    print('É possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo!')

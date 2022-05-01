valor = float(input('Uma distancia em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('A medida de {}m Corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(valor, km, hm, dam, dm, cm, mm))

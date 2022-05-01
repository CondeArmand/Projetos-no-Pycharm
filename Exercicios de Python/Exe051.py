pri = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão: '))
for c in range(0, 10):
    print(pri + c * raz,'->', end=' ')
print('Acabou')
termo = 0
while termo <= 0:
    termo = int(input('Até que termo vc deseja a série de Fibonacci? '))
    if termo <= 0:
        print('O termo informado deve ser positivo!')

primeiro = 0
print(primeiro, end=' ')
segundo = 1
for i in range(1, termo):
    print(segundo, end=' ')
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
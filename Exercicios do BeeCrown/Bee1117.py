while True:
    nota1 = float(input())
    if 10 >= nota1 >= 0:
        break
    else:
        print('nota invalida')
while True:
    nota2 = float(input())
    if 10 >= nota2 >= 0:
        break
    else:
        print('nota invalida')
media = (nota1 + nota2)/2
print('media = {}'.format(media))

s1 = float(input('Informe o primeiro seguimento: '))
s2 = float(input('Informe o segundo seguimento: '))
s3 = float(input('Informe o terceiro seguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É possivel formar um triangulo!')
    if s1 == s2 == s3:
        print('É um triangulo EQUILÁTERO.')
    if s1 != s2 != s3 != s1:
        print('É um triangulo ESCALENO.')
    else:
        print('É um triangulo ISÓCELES.')
else:
    print('Não é possivel formar um triangulo!')


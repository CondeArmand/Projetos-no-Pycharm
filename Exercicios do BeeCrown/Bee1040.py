notas = map(float, input().split())
N1, N2, N3, N4 = notas
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/10
if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
else:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    mediafinal = (media + exame)/2
    if mediafinal >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(mediafinal))

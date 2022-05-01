num_alunos = 4
i = 1
media = 0
while i <= num_alunos:
    nota = float(input('Digite sua nota ' + str(i) + ': '))
    media = media + nota
    i = i + 1
media = media / num_alunos
print('Media {:.1f}'.format(media))

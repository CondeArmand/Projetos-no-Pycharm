from math import sqrt
while True:
    try:
        nums = map(int, input().split(' '))
        D, VF, VG = nums
        hip = sqrt(D ** 2 + 12 ** 2)
        TVF = 12 / VF
        TVG = hip / VG
        if TVG <= TVF:
            print('S')
        else:
            print('N')
    except EOFError:
        break

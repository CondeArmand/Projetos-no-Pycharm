posi = 0
med = 0
for n in range(0, 6):
    num = float(input())
    if num >= 0:
        posi = posi + 1
        med = med + num
print('{} valores positivos'.format(posi))
print('{:.1f}'.format(med/posi))

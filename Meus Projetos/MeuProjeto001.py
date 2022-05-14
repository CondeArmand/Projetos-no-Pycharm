x = 9
for i in range(9):
    x = x + 2
    print(x, end=' ')
    if i < 4:
        continue
    x = x - i
    print(x, end=' ')

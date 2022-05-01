T = int(input())
N = []
for i in range(1000):
    X = 0
    while X < T:
        N.append(X)
        X += 1
    print('N[{0}] = {1}'.format(i, N[i]))

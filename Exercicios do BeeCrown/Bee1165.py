n = int(input())
for c in range(0, n):
    num = int(input())
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                print('{} nao eh primo'.format(num))
                break
        else:
            print('{} eh primo'.format(num))
    else:
        print('{} nao eh primo'.format(num))

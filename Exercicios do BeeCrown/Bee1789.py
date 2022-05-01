while True:
    try:
        L = int(input())
        lista = map(int, input().split(' '))
        MV = max(lista)
        if MV < 10:
            print(1)
        elif 10 <= MV < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break

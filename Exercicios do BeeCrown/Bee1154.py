x = 0
y = 0
media = 0
while x >= 0:
    x = int(input())
    media += x
    y += 1
print('{:.2f}'.format((media + (-x)) / (y - 1)))

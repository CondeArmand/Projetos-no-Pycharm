tam = 5
x = []
y = []
z = []
for i in range(tam):
    x.append(input('Digite (x): '))
for i in range(tam):
    y.append(input('Digite (y): '))
for i in range(tam):
    z.append(x[i])
    z.append(y[i])
print(z)
x = 1
n = int(input('Digite um número para ver sua tabuada: '))
for x in range(x, 11):
    print('{} x {} = {}'.format(n, x, n * x))
    x += 1
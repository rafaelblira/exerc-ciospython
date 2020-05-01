soma = 0
cont = 0
for n in range(0, 501, 3):
    if n % 2 != 0:
        cont += 1
        soma += n
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
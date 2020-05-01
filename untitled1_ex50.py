soma = 0
cont = 0
for c in range(1, 7):
    nun = int(input('Digite o {}º valor: '.format(c)))
    if nun % 2 == 0:
        soma += nun
        cont += 1
print('Você somou {} pares e a soma foi de {}'.format(cont, soma))

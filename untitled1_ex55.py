c = 1
lista = []
for c in range (1, 6):
    peso = float(input('O peso da {}ª pessoa: '.format(c)))
    lista +=[peso]
print('O maior peso foi: {}kg'.format(max(lista)))
print('O menor peso foi: {}kg'.format(min(lista)))

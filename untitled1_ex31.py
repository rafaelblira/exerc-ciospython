km = int(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(km))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('E o preço da passagem será de R${:.2f}'.format(preco))

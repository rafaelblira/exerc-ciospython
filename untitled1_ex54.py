from datetime import date
atual = date.today().year
c=1
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Ao todo tivemos {} maiores de idade'.format(maiores))
print('E também tivemos {} menores de idade'.format(menores))


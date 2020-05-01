from datetime import date
atual = date.today().year
ano = int(input('Qual o ano de seu nascimento? '))
idade = atual - ano
falta = atual + (18 - idade)
if idade < 18:
    print('Você tem {} anos e deverá se alistar no ano de {}'.format(idade, falta))
elif idade == 18:
    print('Você deverá se alistar neste ano')
else:
    print('Você tem {} anos e já passou da idade de se alistar'.format(idade))
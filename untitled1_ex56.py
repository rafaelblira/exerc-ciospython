c = 1
mulheres = 0
somaidade = 0
madia = 0
maioridadehomem = 0
nomevelho = ''
for c in range(1, 5):
    print('------{}ª PESSOA -------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).upper()
    somaidade += idade
    media = somaidade / 4
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade >  20:
        mulheres += 1
print('A média de idade do grupo é de {:.2f}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))


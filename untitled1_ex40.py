n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
    print('O aluno está APROVADO')
elif media > 5 and media <= 6.9:
    print('Tirando {} e {}, sua média é {}'. format(n1, n2, media))
    print('O aluno está de RECUPERAÇÃO')
else:
    print('Tirando {} e {}, sua média é {}'.format(n1, n2, media))
    print('O aluno está REPROVADO')
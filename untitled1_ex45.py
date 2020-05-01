from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções: ')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
opcao = int(input('Qual a sua opção? '))
if opcao == 0 or opcao == 1 or opcao == 2:
    print('=-' * 20)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)
    print('=-' * 20)
    print('O computador escolheu {}'.format(itens[computador]))
    print('Você escolheu {}'.format(itens[opcao]))
    if computador == 0 and opcao == 1:
        print('Você ganhou!')
    elif computador == 1 and opcao == 2:
        print('Você ganhou!')
    elif computador == 2 and opcao == 0:
        print('Você ganhou')
    elif computador == 1 and opcao == 0:
        print('Você perdeu!')
    elif computador == 2 and opcao == 1:
        print('Você perdeu!')
    elif computador == 0 and opcao == 2:
        print('Você perdeu!')
    elif computador == opcao:
        print('Empatou!')
else:
    print('Jogada inválida')

from random import randint
cont = 1
nun = 0
computador = randint(0,10)
print('Sou seu computador . . . ')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')
num = int(input('Qual é seu palpite? '))
while nun != computador:
    if nun > computador:
        print('Menos ... Tente mais uma vez. ')
        nun = int(input('Qual é seu palpite? '))
    elif nun < computador:
        print('Mais ... Tente mais uma vez.')
        nun = int(input('Qual é seu palpite? '))
    cont += 1
print('Acertou com {} tentativas. Parabéns!'.format(cont))


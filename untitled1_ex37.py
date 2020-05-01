nun = int(input('Digite um número inteiro: '))
print('''Escolha um número para conversão:'
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(nun, bin(nun)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(nun, oct(nun)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'. format(nun, hex(nun)[2:]))
else:
    print('Opção inválida')
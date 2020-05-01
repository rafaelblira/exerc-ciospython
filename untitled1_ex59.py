nun1 = int(input('Primeiro valor: '))
nun2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = nun1 + nun2
        print('O resultado de {} + {} é {}'.format(nun1, nun2, soma))
    elif opcao == 2:
        mult = nun1 * nun2
        print('O resultado de {} x {} é {}'. format(nun1, nun2, mult))
    elif opcao == 3:
        if nun1 > nun2:
           print('O maio valor é {}'.format(nun1))
        if nun1 == nun2:
           print('Os números são iguais')
        else:
            print('O vamior valor é {}'.format(nun2))
    elif opcao == 4:
         print('Informe os números novamente')
         nun1 = int(input('Primeiro valor: '))
         nun2 = int(input('Segundo valor: '))
    elif opcao == 5:
         print('Fim do programa, volte sempre!!!')
    else:
         print('Opção inválida, tente novamente')


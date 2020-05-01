print('='*10, 'LOJAS GUANABARA', '='*10)
valor = float(input('Qual o valor das compras? '))
print('[1] A vista dinheiro ou cheque')
print('[2] A vista no cartão')
print('[3] Parcelado em até 2 vezes no cartão')
print('[4] Parcelado em 3x ou mais no cartão')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
    print('Sua compra custará R${:.2f} a vista'.format(valor * 0.9))
elif opcao == 2:
    print('Sua compra custará R${:.2f} a vista no cartão'. format(valor * 0.95))
elif opcao == 3:
    print('Sua compra custará R$ {:.2f} em 2x no cartão'.format(valor))
elif opcao == 4:
    print('Sua compra custará R$ {:.2f} em 3 vezes ou mais no cartão'. format(valor * 1.2))
else:
    print('Opção inválida')

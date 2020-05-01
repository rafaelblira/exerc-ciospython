casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Qantos anos de financiamento? '))
meses = anos * 12
parcela = casa / meses
if parcela > salario * 0.3:
    print('O financiamento foi REPROVADO')
else:
    print('Sua prestação será  de R${:.2f} em {} anos.'.format(parcela, anos))
    print('O financiamento foi APROVADO')
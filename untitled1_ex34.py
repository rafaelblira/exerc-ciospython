salario = float(input('Qual é o salário do funcionário? '))
if salario >= 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
print('Quem ganhava R$ {:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))
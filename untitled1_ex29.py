velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((velocidade-80)*7))
print('Tenha um bom dia! Dirija com segurança!')
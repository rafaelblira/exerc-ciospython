sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))


print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('O triângulo é equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo é isóceles')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('O triângulo é escaleno')
else:
    print('Não formam um triângulo')
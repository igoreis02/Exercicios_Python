quilometro = float(input('Qual a distância em km da viagem? '))
print('Você está preste a começar uma viagem de {:.1f} km'.format(quilometro))
if quilometro <= 200:
    valor = quilometro * 0.50
    print('O preço da sua passagem será de R${:.2f}'.format(valor))
else:
    valor = quilometro * 0.45
    print('O preço da sua passagem será de R${:.2f}'.format(valor))

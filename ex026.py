velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade >80:
    multa = (velocidade-80) * 7.0
    print('MULTADO! Você exedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia!Dirija com segurança ')

nome = str(input('Qual o seu nome completo? '))
formatar = nome.split()
print('Seu primeiro nome é: {} '.format(formatar[0].upper()))
print('O ultimo nome é: {}'.format(formatar[len(formatar)-1]).upper())

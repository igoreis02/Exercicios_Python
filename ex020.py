nome = str(input('Qual o seu nome: '))
print('Analisando seu nome... ')
print('Seu nome em maiúsculas è ', nome.upper())
print('Seu nome em minúsculas è ', nome.lower())
print('Seu nome tem ao todo ', len(nome.strip()), 'letras ')
separacao = nome.split()
print('Seu primeiro nome é ', separacao[0], 'e ele tem ', len(separacao[0]), 'letras')


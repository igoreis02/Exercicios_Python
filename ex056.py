media = 0
soma = 0
nome = ''
mulheres = 0
mais_velho = 0
for c in range(1, 5):
    nomep = str(input('Qual o seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? F/M'))
    soma += idade
    if c == 1 and sexo in 'Mm':
        mais_velho = idade
        nome = nomep
    if idade > mais_velho and sexo in 'Mm':
        nome = nomep
        mais_velho = idade
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
media = soma/4
print('''A media de idade é {}
o homem mais velhor é {} 
a quantidade de mulheres menores de 20 anos sao {}'''.format(media, nome,mulheres))

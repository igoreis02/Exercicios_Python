from datetime import  date
qtdMaior = 0
qtdMenor = 0
for c in range(1, 7):
    data = int(input('Qual a sua data de nascimento? '))
    data_atual = date.today().year
    idade = data_atual - data
    if idade > 18:
        qtdMaior += 1
    else:
        qtdMenor += 1
print('{} pessoas vao atingir a maior idade:'.format(qtdMenor))
print('{} pessoas já estão de maior:'.format(qtdMaior))

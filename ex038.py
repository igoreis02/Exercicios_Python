from datetime import date
ano_nascimento = int(input('Qual seu ano de nascimento ?'))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
print('Sua idade é {} anos '.format(idade))
print('Categoria: ')
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade < 14:
    print('INFANTIL')
elif idade > 14 and idade < 19:
    print('JUNIOR')
elif idade > 19 and idade < 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
else:
    print('INVÁLIDO')

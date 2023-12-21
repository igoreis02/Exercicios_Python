from datetime import date
anoNascimento = int(input('Qual o seu ano de nascimento?'))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    saldo = 18 - idade
    ano = anoAtual + saldo
    print('Você ainda não pode realizar o alistamento falta {} anos '.format(saldo))
    print('Seu alistamento é em {}'.format(ano))
elif idade == 18:
    print('Esta na data de realizar o alistamento! ')
elif idade > 18:
    saldo = idade - 18
    ano = anoAtual + saldo
    print('Já passou a data de fazer o alistamento!')
    print('Você já deveria ter se alistado  há  {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Inválido')



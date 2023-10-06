salario = float(input('Qual o seu salário do funcionário? R$'))
if salario > 1250:
    aumento = salario + (salario*10/100)
    print('Quem ganha R${:.2f} passa a ganha R${:.2f} agora.'.format(salario, aumento))
if salario <= 1250:
    aumento = salario + (salario*15/100)
    print('Quem ganha R${:.2f} passa a ganha R${:.2f} agora.'.format(salario, aumento))

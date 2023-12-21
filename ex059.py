num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))

opc = 0
while opc != 5:
    print('''
    [1] SOMAR')
    [2] MULTIPLICAR')
    [3] MAIOR')
    [4] NOVOS NÚMEROS')
    [5] SAIR''')
    opc = int(input('Digite a opção: '))

    if opc == 1:
        soma = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1, num2, soma))
    elif opc == 2:
        multiplica = num1 * num2
        print('A Multiplicação entre {} * {} = {}'.format(num1, num2, multiplica))
    elif opc == 3:
        if num1 > 0 and num2 > 0:
            if num1 > num2:
                print('O maior é {}'.format(num1))
            elif num2 > num2:
                print('O maior é {}'.format(num2))
            else:
                print('São iguais!')
    elif opc == 4:
        num1 = int(input('Digite o 1º valor: '))
        num2 = int(input('Digite o 2º valor: '))
    elif opc == 5:
        print('Obrigado por usar nosso sistema!')
    else:
        print('Opção invalida,  tente novamente ')

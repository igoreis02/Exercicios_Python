numero = ('zero', 'Um', 'Dois', 'Três', 'Quarto',
          'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
          'Dez', 'Onze', 'Doze', 'Treze', 'Quatrorze',
          'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

opc = 's'
while opc == 's':
    while True:
        num = int(input('Digite um numero ente 0 e 20: '))
        if 20 >= num >= 0:
            break
        print('Tente novamente.', end='')
    print(f'Você digitou o número {numero[num]}')
    opc = str(input('Você quer continuar: s/n')).lower()
    while opc not in 'ns':
        opc = str(input('Tente novamente. Você quer continuar: s/n')).lower()


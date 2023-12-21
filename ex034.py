num = int(input('Digite um número! '))
print('='*20)
print(''' Escolha qual a conversão:
 1 - Converter para Binário
 2 - Converter para Octal
 3 - Converter para Hexadecimal''')
print('='*20)
opc = int(input('Escolha um opção!'))

if opc == 1:
    print('Binário {}'.format(bin(num)[2:]))
elif opc == 2:
    print('Octal {}'.format(oct(num)[2:]))
elif opc == 3:
    print('Hexadecimal {}'.format(hex(num)[2:]))
else:
    print('Opção inválida')

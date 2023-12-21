num1 = int(input('Digite um número inteiro! '))
num2 = int(input('Digite outro número inteiro! '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo é maior')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais!')
else:
    print('invalido')

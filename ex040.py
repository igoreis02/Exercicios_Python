preco = float(input('Qual o valor do Produto?'))
print('='*20)
print('Qual a forma de pagamento?')
print('1 - dinheiro ou cheque')
print('2 - Cartão à vista')
print('3 - 2x cartão de credito')
print('4 - 3 ou mais vezes no cartão')
print('='*20)
opc = int(input('Selecione uma opção: '))

if opc == 1:
    desconto = (preco * 10)/100
    print('O valor do produto com desconto de 10% é R${}'.format(preco-desconto))
elif opc == 2:
    desconto = (preco * 5)/100
    print('O valor do produto com o desconto de 5% é R${}'.format(preco-desconto))
elif opc == 3:
    print('O valor do produto é R${} '.format(preco))
elif opc == 4:
    juros = (preco * 20)/100
    print('O valor do produto com o juros de 20% é R${}'.format(preco+juros))
else:
    print('Invalido')

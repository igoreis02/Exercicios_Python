num = 0
soma = 0
qtd = 0
while num != 999:
    num = int(input('Digite um número [999 para sair]:'))
    if(num != 999):
        soma += num
        qtd += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(qtd, soma))

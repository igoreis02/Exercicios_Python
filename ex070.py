opc = 'S'
total = maisM = menor = cont = 0
nome = ' '
while opc == 'S':
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    total += valor
    cont += 1
    if valor > 1000:
        maisM += 1
    if cont == 1:
        menor = valor
    else:
        if valor < menor:
            nome = produto
            menor = valor

    opc = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    while opc not in 'SN':
        opc = str(input('Deseja continuar [S/N]')).upper().strip()[0]
print('-'*20)
print('Fim do programa')
print(f'O total da compra foi R$ {total}')
print(f'Temos {maisM} produtos custando mais de 1000.00')
print(f'O produto mais barato foi {nome} custando R$ {menor}')

lista = list()
cont = 0;

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar.')
    opc = str(input('Deseja continuar? SN')).lower()
    while opc not in 'sn':
        opc = str(input('Tente novamente: Deseja continuar? SN')).lower()
    if opc in 'n':
        break
lista.sort()
print(f'Você digitou os valores : {lista}')

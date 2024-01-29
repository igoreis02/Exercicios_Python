lista = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Adicionado com sucesso!')
    else:
        print('Valor Duplicado, não vou adicionar!')
    opc = str(input('Deseja continuar? [S/N]')).upper()
    while opc not in 'SN':
        opc = str(input('Tente novamente: Deseja continuar? [S/N]')).upper()
    if opc in 'N':
        break

print('='*30)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')

tupla = (int(input('Digite o 1ª valor: ')),
        int(input('Digite o 2ª valor: ')),
        int(input('Digite o 3ª valor: ')),
        int(input('Digite o 4ª valor: ')))

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posiçao')
else:
    print('O valor 3 não fou digitado em nenhuma posição')
par = 0
print(f'Os valores Pares digitados foram:', end='')
for cont in tupla:
    if cont % 2 == 0:
        print(cont, end=' ')

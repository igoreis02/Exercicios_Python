num = list()
maior = menor = ant = 0
for cont in range(0,5):
    num.append(int(input(f'Digite o {cont+1}ª valor: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print(f'Você digitou os valores {num}')
print(f'O maior Número da lista foi: {maior} na posição ', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i+1}...',end='')
print(f'\nO menor número da lista foi: {menor} na posição ',end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i+1}...',end='')

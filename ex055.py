maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o seu peso?'))
    if c == 1:
        menor = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi: {} kg'.format(maior))
print('O menor peso foi: {} kg'.format(menor))

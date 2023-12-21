cond = 'S'
comp = 0
cont = soma = media = maior = menor =0
while cond == 'S':
    num = int(input('Digite um número: '))
    cond = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
media = soma/cont
print('Você digitou  {} números e a média foi {}'.format(cont, media))
print('o Maior valor foi {} e o menos foi {}'.format(maior, menor))


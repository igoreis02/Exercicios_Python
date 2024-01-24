qtd50 = qtd20 = qtd10 = qtd1 = resto = 0
valor = int(input('Qual valor deseja sacar?'))
while True:
    if valor > 50:
        qtd50 = int(valor / 50)
        resto = valor % 50
        if resto == 0:
            break
        if resto >= 20:
            qtd20 = int(resto/20)
            resto = resto % 20
        if resto == 0:
            break
        if resto >= 10:
            qtd10 = int(resto/10)
            resto = resto % 10
            if resto == 0:
                break
        if resto >= 1:
            qtd1 = int(resto/1)
            resto = resto % 1
            if resto == 0:
                break
print(f'Total de {qtd50} cédulas de R$50')
print(f'Total de {qtd20} cédulas de R$20')
print(f'Total de {qtd10} cédulas de R$10')
print(f'Total de {qtd1} cédulas de R$1')

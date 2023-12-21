num = soma = quant = 0
while num != 999:
    num = int(input('Digite um nùmero: [999 para sair]'))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'Foram digitados {quant} e a soma entre eles é {soma}')

cont = 1
result = 0
num = int(input('Qual taboada?'))
while num > 0:
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        result = num * cont
        print(f'{cont} x {num} = {result}')
        cont += 1
    num = int(input('Qual taboada?'))
print('Programa Tabuada encerrado!')

def leiaInt(msg):
    while True:
        try:
            n = str(input(msg))
            n = int(n)
            return n
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg)).replace(',','.')
            n = float(n)
            return n
        except:
            print('\033[0;31mERRO! Digite um número Real válido\033[m')


numi = leiaInt('Digite um valor inteiro: ')
numr = leiaFloat('Digite um Valor Real')
print(f'O número Inteiro Digitado foi {numi} Real foi {numr}')

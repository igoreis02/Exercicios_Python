def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m Usuário preferiu  não digitar esse número')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg)).replace(',','.')
            n = float(n)
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número Real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m Usuário preferiu  não digitar esse número')
            break
        else:
            return n


numi = leiaInt('Digite um valor inteiro: ')
numr = leiaFloat('Digite um Valor Real')
print(f'O número Inteiro Digitado foi {numi} Real foi {numr}')

def leiaInt(msg):
    while True:
        try:
            opc = int(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31mUsuário decidiu para o programa.\033[m')
        except:
            print('\033[0;31mErro: por favor, Digite um número inteiro Válido.\033[m')
        else:
            return opc


def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc





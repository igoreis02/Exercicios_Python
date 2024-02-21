def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return n


n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')

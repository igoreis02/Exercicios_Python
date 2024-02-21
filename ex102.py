def fatorial(num, show=False):
    '''
    -> Fatorial de um numero
    :param num:  valor do fatorial
    :param show: mostra a repetiçao
    :return: o valor da multiplicação
    '''
    print('-'*30)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c != 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


print(fatorial(5,True))

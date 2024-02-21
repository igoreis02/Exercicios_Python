from time import sleep


def maior(*num):
    print('='*40)
    maior = 0
    print('Analizando os valores passados...')
    for k, c in enumerate(num):
        if k == 0:
            maior = c
        if c > maior:
            maior = c
        sleep(0.5)
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram passados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

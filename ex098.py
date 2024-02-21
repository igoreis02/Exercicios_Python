from time import sleep
def escreva():
    print('=' * 30)


def contador(i,f,p):
    escreva()
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        for c in range(i, f+1, p):
            sleep(0.5)
            print(c, end=' ')
        print('Fim')
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(cont,end=' ')
            cont -= p
        print('Fim')


#Programa Principal
contador(1,10,1)
contador(10,0,2)
escreva()
print('Agora é sua vez de personalizar a contagem! ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
contador(i, f, p)

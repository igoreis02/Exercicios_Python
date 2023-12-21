n = int(input('Quantos temos você quer mostrar?'))
t1 = 0
t2 = 1
cont = 3
fibonacci = 0
print('{} - {} -'.format(t1, t2))
while cont <= n:
    t3 = t1 + t2
    print('{} - ' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1


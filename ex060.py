num = int(input('Digite o fatorial: '))
f = 1
c = num
while c > 0:
    f = f * c
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    c -= 1
print(f)

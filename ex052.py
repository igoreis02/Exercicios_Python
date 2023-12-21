num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('{} É PRIMO'.format(c))
        tot += 1
    else:
        print('{} NÃO É PRIMO'.format(c))
print('O número {} foi divisivel {} vezes '.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')

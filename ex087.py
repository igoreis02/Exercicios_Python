matriz =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = soma3 = maiorl = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
        if matriz[l][c]%2 == 0:
            somaPar = somaPar + matriz[l][c]
        if c == 2:
            soma3 = soma3 + matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorl:
                maiorl = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira colune é {soma3}')
print(f'O maior valor da segunda linha é {maiorl}')

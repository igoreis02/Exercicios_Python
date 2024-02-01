valor = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = input(f'Digite um valor para [{c}] [{i}]')

for c in range (0,3):
    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()

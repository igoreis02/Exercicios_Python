from random import randint
soma = 0
qtd = 0
print('Vamos jogar PAR OU IMPAR')
print('-'*20)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    cond = str(input('PAR OU IMPAR [P / I]')).upper().strip()[0]
    while cond not in 'PI':
        cond = str(input('PAR OU IMPAR [P / I]')).upper().strip()[0]
    soma = computador + jogador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}, Total {soma} deu Par')
    if soma % 2 == 1:
        print(f'Você jogou {jogador} e o computador {computador}, Total {soma} deu Impar')
    if cond == 'P':
        print('Você Ganhou')
        qtd += 1
    else:
        print('Você perdeu')
        break
print(f'Game Over! Você venceu {qtd} vezes')

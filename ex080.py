lista = list()

for cont in range(0,5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adiconado na posição {pos} da lista ')
                break
            pos += 1;
print(f'Os valores digitados em ordem foram {lista}')

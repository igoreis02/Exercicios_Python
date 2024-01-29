exp = str(input('Digite a expressão: '))
pilha = list()

for simbulo in exp:
    if simbulo == '(':
        pilha.append('(')
    elif simbulo == ')':
        if len(pilha) > 0:
            pilha.pop() #remove o ultimo elemento
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta válida')
else:
    print('Sua expressao esta errada')

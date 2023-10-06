frase = str(input('Digite uma frase')).upper()
print('a letra A apareceu {} vezes na frase:' .format(frase.count('A')))# count pega a quantidade de letras a
print('a primeiro letra A  apareceu na posição {}'.format(frase.find('A')+1))#find pega a primeira letra a colocada
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))# rfind procura a partir do lado direiro rand

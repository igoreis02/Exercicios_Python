def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() # converte as virgulas para ponto
        if entrada.isalpha() :#or entrada.strip() == '':  ## testa de é alfa numerico ou retira todos os espacoes com o strip e ver se é vazio
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m;')
        else:
            valido = True
            return float(entrada)
time = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo',
        'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
        'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians',
        'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(f'Os 4 primeiro colocados da tabela são: {time[0:5]}')
print(f'Os 4 Utimos colocados são: {time[-4:]}')
print(f'Os times em ordem alfabeticas {sorted(time)}')
print(f'A posição do palmeiras na Lista é: {time.index("Palmeiras")+1}')

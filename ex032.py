print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
primeiro = float(input('Primeiro segmento'))
segundo = float(input('Segundo segmento'))
terceiro = float(input('Terceiro segmento'))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    print('os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

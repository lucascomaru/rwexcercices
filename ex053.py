frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join((palavras))
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('A frase é um palíndromo! ')
else:
    print('A frase não é um palíndromo')
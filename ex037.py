num = int(input('Digite um número inteiro: '))
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
conv = int(input('Sua opção: '))
if conv == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')
elif conv == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif conv == 3:
    print(f'{num}convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opcão inválida, tente novamente! ')


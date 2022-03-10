num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
        print('', end='')
    else:
        print('', end='')
print(f'O número {num} foi divisível {total} vezes ')
if total == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
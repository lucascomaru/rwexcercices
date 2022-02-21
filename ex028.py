from random import choice
p = int(input('Em qual número eu pensei? '))
lista = [1, 2, 3, 4, 5]
cpu = choice(lista)
if p == cpu:
    print('Parabéns! Você acertou o número que pensei! ')
else:
    print(f'Você errou o número que eu pensei! Eu pensei no número {cpu} ')
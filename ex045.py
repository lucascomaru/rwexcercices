import random
print("""Suas opções: 
[1]Pedra
[2]Papel
[3]Tesoura """)
jogada = input('Qual a sua jogada? ')
jogador = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0,2)
print(jogador[pc])

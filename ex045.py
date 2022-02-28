from random import randint
jogo = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print("""Suas opções: 
[1]Pedra
[2]Papel
[3]Tesoura """)
jogada = int(input('Qual a sua jogada? '))
print(f'O computador escolheu {jogo[pc]}')
print(f'O jogador escolheu {jogo[jogada]}')
if pc == 0:  #PC JOGANDO PEDRA
    if jogada == 0:
        print('EMPATE! ')
    elif jogada == 1:
        print('JOGADOR VENCEu!')
    elif jogada == 2:
        print('COMPUTADOR VENCEU! ')
    else:
        print('JOGADA INVÁLIDA! ')
elif pc == 1:
    if jogada == 0:
        print('COMPUTADOR VENCEU! ')
    elif jogada == 1:
        print('EMPATOU! ')
    elif jogada == 2:
        print('JOGADOR VENCEU! ')
    else:
        print('JOGADA INVÁLIDA! ')
elif pc == 2:
    if jogada == 0:
        print('JOGADOR VENCE!')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
vel = int(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Siga em segurança!')
else:
    print(f'Você ultrapassou o limite de velocidade, você terá que pagar {multa} Reais')
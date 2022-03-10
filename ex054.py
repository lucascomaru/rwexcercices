from datetime import date
cmenor = 0
cmaior = 0
atual = date.today().year
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c} pessoa nasceu?'))
    hoje = atual - nascimento
    if hoje <18:
        cmenor+= 1
    else:
        cmaior += 1
print(f'O número de pessoas menor de idade foi de {cmenor}')
print(f'O número de pessoas maior de idade foi de {cmaior}')
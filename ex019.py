import random
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
lista = [pa, sa, ta, qa]
escolhido = random.choice(lista)
print(f'O escolhido foi: {escolhido}')

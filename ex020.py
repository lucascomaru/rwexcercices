import random
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
lista = [pa, sa, ta, qa]
random.shuffle(lista)
print(f'A ordem de apresentação é: {lista}')
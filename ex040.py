n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('O aluno está reprovado! ')
elif 7 > média >=5:
    print('O aluno está de recuperação! ')
else:
    print('O aluno está APROVADO')
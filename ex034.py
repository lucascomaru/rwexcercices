salario = float(input('Digite o salário do funcionário: '))
aumento = salario+ (salario * 10) / 100
aumento2 = salario+  (salario *15) / 100
if salario >= 1250:
    print(f'O novo salário do funcionário é de {aumento}')
else:
    print(f'O novo salário do funcionário é {aumento2}')
casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Anos de financiamento: '))
valor = casa / (anos * 12)
minimo = salario * 30/100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de {valor:.2f}')
if valor <=minimo:
    print('Empréstimo CONCEDIDO! ')
else:
    print('Empréstimo NEGADO! ')
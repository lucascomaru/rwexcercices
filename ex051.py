termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = termo + (10 - 1) * razao
s = termo
for num in range(termo, décimo + razao, razao):
    print(num)
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
if v1 <= v2 and v3:
    menor = v1
if v2 <= v1 and v3:
    menor = v2
if v3 <= v1 and v2:
    menor = v3
if v1 >= v2 and v3:
    maior = v1
if v2 >= v1 and v3:
    maior = v2
if v3 >= v1 and v2:
    maior = v3
print(f'O maior menor número é {maior} ')
print(f'O menor número é {menor} ')

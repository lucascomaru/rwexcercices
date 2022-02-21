dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
diaria = (dias * 60)
quilometragem = km * 0.15
total = diaria + quilometragem
print(f'O total a pagar é de: R${total:.2f}')
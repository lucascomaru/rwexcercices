produto = float(input('Qual é o preço do produto? R$: '))
promo = produto - (produto * 5 / 100)
print(f'O produto que custava {produto} na promoção com desconto de 5% vai custar {promo}')
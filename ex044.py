preço = float(input('Preço das compras: '))
print("""Formas de pagamento'
      '[1]A vista dinheiro/cheque'
      '[2]A vista cartão'
      '[3]2x no cartão'
      '[4]3x ou mais no cartão""")
opção = int(input('Qual é a opção? '))
if opção == 1:
      saldo = preço - (preço * 10)/100
      print(f'Sua compra de R$ {preço} com 10% de desconto vai custar R$ {saldo}')
if opção == 2:
      saldo = preço - (preço * 5)/ 100
      print(f'Sua compra de R$ {preço} com 5 % de desconto vai custar R$ {saldo}')
if opção == 3:
      saldo = preço
      parcela = saldo / 2
      print(f'Sua compra no valor de R$ {preço} pago em 2x de R$ {parcela} custará R$ {preço}')
if opção == 4:
      saldo = preço + (preço * 20)/100
      print(f'Sua compra no valor de R$ {preço} com juros de 20% vai custar R$ {saldo}')

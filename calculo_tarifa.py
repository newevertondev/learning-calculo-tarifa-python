mn= int(input('Quantos minutos? '))

if mn <= 100:
    valor = 100.00
else:
    valor = 50.00 + (mn - 100) * 2.00

print('Valor a pagar: R$ {:.2f}'.format(valor))


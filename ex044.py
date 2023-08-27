preco = float(input('Valor do produto: R$'))
cond = input('Condição de pagamento:\n1 - Á vista\n2- 1x Cartão\n3 - 2x no Cartão\n4 - 3x no cartão\n')
if cond == '1':
    print('Valor a pagar R$ {} á vista.'.format(preco*0.9))
elif cond == '2':
    print('Valor a pagar R$ {} no cartão'.format(preco*0.95))
elif cond == '3':
    print('Valor a pagar R$ {} 2x no cartão'.format(preco))
elif cond == '4':
    print('Valor a pagar R$ {} 3x no cartão'.format(preco*1.2))
else:
    print('Digite algo válido!')
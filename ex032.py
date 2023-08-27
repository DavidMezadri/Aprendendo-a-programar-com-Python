a = int(input('Digite um ano qualquer: '))
if a % 4 == 0:
    print('{} é um ano bissexto!'.format(a))
else:
    print('{} não é um ano bissexto!'.format(a))
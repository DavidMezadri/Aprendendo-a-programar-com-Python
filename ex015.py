km = float(input('Quantos quilômetros foram rodados: '))
d = float(input('Quantos dias alugados: '))
v = km*0.15+d*60
print('O valor a pagar é: R${:.2f}'.format(v))
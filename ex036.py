valor_casa = float(input('Qual o valor da casa que deseja comprar? '))
valor_salario = float(input('Qual o valor do seu sálario? '))

if (valor_casa/600) <= (valor_salario*0.3):
    print('Parabens você pode comprar essa casa.')
else:
    print('Você não pode comprar essa casa, pois a parcela excede {} reais dos 30% do seu salário!'.format((valor_casa/600)-(valor_salario*0.3)))
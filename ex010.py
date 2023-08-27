#Cotaçao do dollar
d = float(input('Digite quantos reais você deseja converter para dollar: '))
c = float(input('Digite a cotaçao do dollar de hoje: '))

print('R${} reais podem ser convertidos ${:.2f} dollars.'.format(d, d/c))

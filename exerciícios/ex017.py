#Calcular a hipotenusa
from math import sqrt, pow
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjascente: '))
print('A o valor da hipotenusa com cateto oposto de valor {} e cateto adjascente {} é: {:.2f}'.format(co, ca, sqrt(pow(co,2)+pow(ca,2))))

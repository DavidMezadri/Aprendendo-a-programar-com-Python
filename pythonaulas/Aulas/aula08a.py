import math
# Quando você importa a biblioteca inteira precisa chamar a biblioteca.função
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}.'.format(num, math.floor(raiz)))

from math import sqrt, floor
# Quando vc importa a funçao da biblioteca, pode chamar somente a funçao
num = int(input("Digite um número: "))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}.'.format(num, floor(raiz)))

import math as m
# Com a palavra-chave 'as' podemos apelidar a biblioteca para uso mais fácil.
print(m.sqrt(16))

#Para acessar as biblioitecas presentes no python basta acessar:
#https://docs.python.org/3/
#Escolher a versão e clicarem referências de bibliotecas

import random
n = random.random()
# gera um número float entre 0 e 1
print(n)
m = random.randint(1, 10)
# randint gera um número inteiro antre um intervalo
print(m)
from random import randint

n_aleatorio = randint(0, 10)
n = 15
print(n_aleatorio)
while n_aleatorio != n:
    n = int(input('Digite um número de 0 a 10 para acertar: '))
    if n_aleatorio == n:
        print('Parabens!! Você acertou, o número era {}!'.format(n_aleatorio))
    elif n_aleatorio != n:
        print('Você errou, tente novamente!!!')
    else:
        print('Alguma coisa deu errado! Reinicie')

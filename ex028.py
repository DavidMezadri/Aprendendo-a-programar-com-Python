from random import randint
n = int(input('Tente advinhar um número de 1 a 5: '))
palpite = randint(1, 5)
if n == palpite:
    print('Parabéns você venceu!!!')
else:
    print('Que pena, você nao acertou! O número correto era {}!'.format(palpite))
from random import randint
pontos = 0
pi = n = 11
print('Jogo par ou impar!')
while True:
    while pi not in [0, 1]:
        pi = int(input('0 - Par e 1 - Impar '))
    while n < 0 or n > 9:
        n = int(input('Digite um número de 0 a 9: '))
    pc = randint(0, 9)
    print(f'Você jogou {n} e o PC jogou {pc}')
    resultado = n + pc
    if resultado % 2 == pi:
        pontos += 1
        print('Boa! Jogue novamente!')
    else:
        break
    pi = n = 11
print(f'Você perdeu e fez {pontos} pontos!')

from random import randint
jogos = []
a = []
n = int(input('Quantos palpites você quer: '))

for i in range(0, n):
    while len(a) < 6:
        b = randint(1, 60)
        if not b in a:
            a.append(b)
    a.sort()
    jogos.append(a)
    a = []
for i in range(0, n):
    print(f'O {i+1} jogo é: {jogos[i]} ')

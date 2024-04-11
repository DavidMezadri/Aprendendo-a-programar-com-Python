from random import randint
jogadores = dict()
maior = 0

for i in range(1, 5):
    jogadores[i] = randint(1, 6)

for j, k in jogadores.items():
    print(f'O jogador {j} tirou {k}')
    if k >= maior:
        maior = k

print('-'*20)

for i in sorted(jogadores, key = jogadores.get):
    print(f'O Jogador {i} tirou {jogadores[i]}')

print('-'*20)

print(f'O maior número tirado foi o {maior} pelo(s) jogadore(s)',end = ' ')
for j, k in jogadores.items():
    if k == maior:
        print(j, end = ' ')


        

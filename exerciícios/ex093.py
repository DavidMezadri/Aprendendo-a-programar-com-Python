lista = dict()
gols = list()
total = 0

lista['nome'] = str(input('Nome do Jogador: '))
a = int(input(f'Quantas patidas {lista["nome"]} jogou? '))
for i in range(0, a):
    gols.append(int(input(f'Quantos gols na partida {i}: ')))
    

lista['gols'] = gols[:]
lista['total'] = sum(lista['gols'])
print(lista, '\n')

print(20*'-=', '\n')

for k, v in lista.items():
    print(f'O campo {k} tem valor {v}.')
print('\n')

print(20*'-=', '\n')

print(f'O jogador {lista["nome"]} jogou {a} partidas.')
for i in range(0, a):
    print(f'   =>  Na partida {i}, fez {lista["gols"][i]} gols.')
print(f'Foi um total de {lista["total"]} gols.')
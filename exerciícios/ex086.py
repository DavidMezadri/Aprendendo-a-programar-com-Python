lista = []
f = 0
for i in range(0, 3):
    for j in range(0, 3):
        a = [int(input(f'Digite o valor da matriz ({i}, {j}): '))]
        lista.append(a)

for t in range(0, 3):
    for u in range(0, 3):
        print(lista[f], end=' ')
        f += 1
    print()

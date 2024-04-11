lista = []
f = pares = terceira = segunda = 0
for i in range(0, 3):
    for j in range(0, 3):
       lista.append(int(input(f'Digite o valor da matriz ({i}, {j}): ')))
        

for t in range(0, 3):
    for u in range(0, 3):
        print([lista[f]], end=' ')
        if lista[f] % 2 == 0:
            pares += lista[f]
        if f > 6:
            terceira += lista[f]
        if f > 2 and f < 6:
            if lista[f] > segunda:
                segunda = lista[f]
        f += 1
    print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha linha é {segunda}')
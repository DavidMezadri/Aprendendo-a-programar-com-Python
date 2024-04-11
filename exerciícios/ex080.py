lista = []
c = 0
for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))
  

for a in range(len(lista)):
    for b in range(len(lista)):
        if lista[a] < lista[b]:
            c = lista[b]
            lista[b] = lista[a]
            lista[a] = c

print(lista)
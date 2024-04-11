lista = [[],[]]

for i in range(1, 8):
    a = int(input(f'Digite o {i}o. número: '))
    if a%2 == 0:
        lista[0] += [a]
    elif a%2 != 0:
        lista[1] += [a]

for j in lista:
    j.sort()
print(f'Os valores pares são: {lista[0]}\nOs valores impares são: {lista[1]}')

lista = []
d = ''
while True:
    a = (input('''Digite um numero a ser adiocionado ou 'p' para parar: '''))
    if a in 'pP':
        break
    lista.append(int(a))

print(f'A lista tem {len(lista)+1} elementos!')

lista.sort(reverse=True)
print(lista)

if 5 in lista:
    for i, c in enumerate(lista):
        if c == 5:
            d += str(i+1) + ' '
    print(f'O valor 5 foi digitado e esta contido no(s) indice(s): {d}')
else:
    print('O valor 5 não foi digitado!')
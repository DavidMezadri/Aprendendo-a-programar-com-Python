n = int(input('Digite um número e direi se ele é primo: '))
z = 0
for c in range(2, 10):
    if n%c == 0 and (n != c and c != 1):
        # não faz nada pq ele é igual a ele mesmo
        z = 1
if 1 == z:
    print('{} não é um número primo!'.format(n))
else:
    print('{} é um número primo!'.format(n))
11
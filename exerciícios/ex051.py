n = int(input('Digite um número: '))
p = int(input('Digite a progressão: '))
for c in range(n, n+(p*10), p):
    print(c, end='➮ ')
print('Acabou!')
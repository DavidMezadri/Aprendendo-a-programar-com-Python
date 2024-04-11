lista = []
pares = []
impares = []

while True:
    a = input('Digite um número: ')
    while not (a.isnumeric()):
        a = input('Digite um número: ')
    lista.append(int(a))
    n = input('Deseja continuar? [S/N] ')
    while n not in 'nNsS':
        n = input('Deseja continuar? [S/N] ')
    if n in 'Nn':
        break

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'A lista com todos os números:\n{lista}')
print(f'Os números pares são:\n{pares}\nOs números ímpares são:\n{impares}')

n1 = int(input(f'Digite o primeiro valor: '))
n2 = int(input(f'Digite o segundo valor: '))
n3 = int(input(f'Digite o terceiro valor: '))
n4 = int(input(f'Digite o quarto valor: '))

npar = 1

tupla = (n1, n2, n3, n4)

print(f'O número 9 aparaceu {tupla.count(9)} vezes.')

if tupla.count(3) > 0:
    print(f'O primeiro numero 3 esta na {tupla.index(3)+1} posição.')
elif tupla.count(3) == 0:
    print('Não temos número 3 nessa tupla.')


for i in tupla:
    if i % 2 == 0:
        npar += 2
        if npar == 3:
            print('Temos os repectivos número(s) par(es): ', end='')
        print(i, end=' ')
        npar = 0
if npar == 1:
    print('Só temos números ímpares nesta tupla.')
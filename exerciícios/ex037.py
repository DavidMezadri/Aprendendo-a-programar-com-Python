n = int(input('Digitre um número que deseja converter: '))
a = int(input('Digite para qual deseja converter: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))
b = ''
if a == 1:
    while n >= 2:
        b = str(n%2) + b
        n = n // 2
    b = str(n%2) + b
    print('Binário: {}'.format(b))
elif a == 2:
    while n >= 8:
        b = str(n%8) + b
        n = n // 8
    b = str(n%8) + b
    print('Octal: {}'.format(b))
elif a ==3:
    while n >= 16:
        e = str(n%16)
        if e == '10':
            e = 'A'
        elif e == '11':
            e = 'B'
        elif e == '12':
            e = 'C'
        elif e == '13':
            e = 'D'
        elif e == '14':
            e = 'E'
        elif e == '15':
            e = 'F'
        b = e + b
        n = n // 16
    b = str(n%16) + b
    print('Hexadecimal: {}'.format(b))
else:
    print('Você digitou algo inválido!')

#int - números inteiros (1,4,12,44..)
#float - números reais (-12.3, 14.5, 7.0)
#bool - valor boleano, sempre primeira letra maisúscula (True, False)
#str - nomes ('Olá, mundo', '')

n = (input('Dingite algo:'))
#.isnumeric é se ele é numerico, se ele piode ser convetido em numerico exemplo: 32
#.isalpha é se ele é letra, exemplo: oi
#.isalhpanum é se ele é numerico e letra, exemplo: 3a, oi, 7
print(n.isnumeric())

#n.isupper - se está em maiúsculo
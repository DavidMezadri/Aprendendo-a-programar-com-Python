l1 = float(input('Digite o valor do primeiro lado do triâgulo: '))
l2 = float(input('Digite o valor do segundo lado do triâgulo: '))
l3 = float(input('Digite o valor do terceiro lado do triâgulo: '))
lista = [l1, l2, l3]
lista.sort()
if lista[0] == lista[1]== lista[2]:
    print('Conseguimos formar um triâgulo, que será equilátero.')
elif lista[0] + lista[1] > lista[2] and lista[0] == lista[1] or lista[2] == lista[1]:
    print('Conseguimos formar um triâgulo, que será isósceles.')
elif (lista[0] + lista[1]) > lista[2]:
    print('Conseguimos formar um triâgulo,onde sua hipotenusa será {} e os catetos serão {} e {}.'.format(lista[2], lista[0], lista[1]))
else:
    print('Não conseguimos formar um triâgulo.')
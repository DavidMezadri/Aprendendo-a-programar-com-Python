n1 = float(input('Digete um número qualquer: '))
n2 = float(input('Digete outro número qualquer: '))
n3 = float(input('Digete mais um número qualquer: '))
l = [n1, n2, n3]
l.sort()
if l[2] != l[0] and l[1] != l[0] and l[1] != l[2]:
    print('O maior valor digitado é {} e o menor é valor digitado é {}.' .format(l[2], l[0]))
elif l[0] == l[1]:
    print('O maior valor digitado é {} e os dois menores valores digitados são {}.'.format(l[2], l[0]))
elif l[1] == l[2]:
    print('Os dois maiores valores digitados são {} e o menor valor digitado é {}.'.format(l[2], l[0]))
else:
    print('Todos os valores são iguas!')


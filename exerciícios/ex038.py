v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
if v1 > v2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(v1, v2))
elif v1 < v2:
    print('O primeiro valor {} é menor que o segundo valor {}'.format(v1, v2))
elif v1 == v2:
    print('O primeiro valor {} é igual ao segundo valor {}'.format(v1, v2))
else:
    print('Algo de errado nao está serto')
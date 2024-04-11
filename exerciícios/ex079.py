lista = []

while True:

    a = (input('''Digite um valor ou 'p' para terminar a lista: '''))

    if a == 'p':
        break
    # se nao tivermos o numero digita dentro da lista entradentro do if para acrescentar o numero
    if int(a) not in lista:
        lista.append(int(a))


print(sorted(lista))
print('terminou')


lista = []
maiores = ''
menores = []
for cont in range(0, 5):
    lista.append(input(f'Digite um valor a ser adicionado na lista na posição {cont+1}: '))


print('-'*40)
for a, b in enumerate(lista):
    print(f'O valor da posiçào {a+1} é {b}')
    # monta os indices maiores na forma de string
    if b == max(lista):
        maiores = str(a) + ' '
    # monta os indices menores na forma de lista
    if b == min(lista):
        menores.append(a)

print('-'*40)
print('\n')
print(f'O maior valor da lista foi {max(lista)} na posição: {maiores}', )
print('\n')
print(f'O menor valor da lista foi: {min(lista)} na posição: ', end='')
#pecorre a lista com os indices menores e imprime
for j in menores:
    print(j, end=' ')
print('\n')
print('-'*40)
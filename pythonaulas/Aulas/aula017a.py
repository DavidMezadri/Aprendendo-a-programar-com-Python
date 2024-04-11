num = [2, 5, 9 , 1]
num[2] = 3
#num[4] = 7   nao conseguimos inserir novo indice desta forma, PHP funciona
num.append(7) # assim conseguimos inserir
num.sort(reverse=True)
num.insert(2, 0) # desta forma pega o indice especificado no primeiro termo da função e joga pra frente e insere o novo
num.pop(2) #remove no indice 2
num.remove(2) # elimina a primeira ocorrencia da lista
print(num)
print(f'Essa lista tem {len(num)} elementos')

# lista = [] ou lista = list()
lista = []
lista.append(5)
lista.append(9)
lista.append(6)

for d in lista:
    print(f'{d}...', end='')
print('\n')
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!!!!')

# adicionar valores dentro da lista
valores = list()
for cont in range(0, 5):
    valores.append(input('Digite um valor para add a lista: '))


a = [2, 3, 4, 7]
#b = a desta forma criamos uma ligação de listas
b = a[:] #desta forma criamos uma copia de 'a' para 'b', ou seja, 'b' recebe o fatiamento de 'a'
b[2] = 8 #python faz uma ligaçao de uma lista e outra, se mudar um valor muda das duas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

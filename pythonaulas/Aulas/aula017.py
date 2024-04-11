lanche = ['picole', 'pizza']
lanche.append('hamburguer') #insere um intem no final da lista
lanche.insert(0, 'cachorro quente') # insere um intem em determinado indice
del lanche[1] # deleta um item em determinado indice
lanche.pop(3) # normalmente o .pop serve para eliminar o ultima elemento, mas podemos passar o indice
lanche.remove('hamburguer') # deleta um intem da lista de acordo com seu conteudo
print(lanche)

#remover a pizza se tivermos este item na lista
if 'pizza' in lanche:
    lanche.remove('pizza')


valores = list(range(4, 11, 2))
print(valores)

lista = [8, 2, 4, 7, 0, 8, 1, 3]
lista.sort() # organiza em ordem crescente
lista.sort(reverse=True) # organiza em ordem decrescente
print(len(lista)) # conta quantos indices preenchido tem na lista, ou seja, numero de incies + 1

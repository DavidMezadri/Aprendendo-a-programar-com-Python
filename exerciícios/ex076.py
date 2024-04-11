lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # temos que diferenciar com aspas simples e duplas
                                     # sempre depois do termo colocar :
                                     # depois do : escrever o caracter que quer ser repetido
                                     # > alinha a esquerda
                                     # < alinha a direita
                                     # ^ centraliza
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}R${lista[i+1]: >8}')
print('-'*40)
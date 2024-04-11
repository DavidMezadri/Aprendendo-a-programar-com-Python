palavras = ('Arvore', 'Abobora', 'Amor', 'Banana', 'Bola', 'Bala', 'Casa', 'Cavalo', 'Carro')

for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i]} temos as vogais: ', end = '')
    for j in palavras[i]:
        if j in 'aeiouAEIOU':
            print(j, end=' ')

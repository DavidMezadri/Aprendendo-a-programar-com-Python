precobarato = c = totalgasto = p1000 = 0
produtobarato = ''
while True:
    nome = input('Digite o nome do produto: ')
    while not nome.isalpha():
        nome = input('Error! Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    c += 1
    if c == 1 or preco < precobarato:
        precobarato = preco
        produtobarato = nome

    totalgasto += preco

    if preco >= 1000:
        p1000 += 1
    a = int(input('Deseja continuar: \n0 - Sim\n1 - Não\n'))
    if a == 1:
        break
print(f'O total gasto foi R$ {totalgasto}\n{p1000} produto(s) custou mais de R$ 1000.00\nO produto mais barato é {produtobarato} custando R$ {precobarato}')


#pergunta = str(input("Quer continuar [S/N]: ")).upper().strip()[0] yn
#if pergunta in "Nn":
    #break
#while pergunta not in "SsNn":
    #pergunta = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
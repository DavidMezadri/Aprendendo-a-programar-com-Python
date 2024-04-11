pessoas = list()
nomemaior = nomemenor = continuar = nome = ''
contador = 0
nome = input('Digite o nome: ')
peso = int(input('Digite o peso: '))
pesomaior = pesomenor = peso
while True:
    lista = [nome, peso]
    #Comparar e armazenar pessoas com amior peso
    if peso == pesomaior:
        nomemaior = nomemaior + nome + ' '
    if peso > pesomaior:
        nomemaior = ''
        nomemaior = nomemaior + nome + ' '
        pesomaior = peso
    
    #Comparar e armazenar pessoas com menor peso
    if peso == pesomenor:
        nomemenor = nomemenor + nome + ' '
    if peso < pesomenor:
        nomemenor = ''
        nomemenor = nomemenor + nome + ' '
        pesomenor = peso
    
    pessoas.append(lista[:])
    contador = contador + 1
    continuar = input('Deseja continuar (S/N): ')
    if continuar in 'nN':
        break
    nome = input('Digite o nome: ')
    peso = int(input('Digite o peso: '))

print(pessoas)
print(f'{contador} pessoas foram cadastradas!')
print(f'O maior peso foi {pesomaior} da(s) pessoa(s): {nomemaior}!')
print(f'O menor peso foi {pesomenor} da(s) pessoa(s): {nomemenor}!')

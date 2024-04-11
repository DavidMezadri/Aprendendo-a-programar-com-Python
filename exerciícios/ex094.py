pessoa = dict()
galera = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] == 'F' or pessoa['sexo'] == 'M':
            break
        print('ERRO! Por favor! Digite M ou F!')

    while True:
        pessoa['idade'] = (input('Idade: '))
        if pessoa['idade'].isnumeric():
            break
        print('ERRO! Por favor! Digite somente números!')
    pessoa['idade'] = int(pessoa['idade'])
    galera.append(pessoa.copy())
    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp == 'S' or resp == 'N':
            break
        print('ERRO! Digite somente S ou N!')
    if resp == 'N':
        break
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas!')
for k in galera:   # O K é 1 dicionario inteiro dentro da lista
    soma += k['idade']  # Soma o item idade do dicionario selecionado por k dentro da lista

print(f'A média das idade é: {soma/len(galera):5.2f}.')

print('As mulheres cadastradas foram: ', end='')
for k in galera:
    if k['sexo'] == 'F':
        print(k['nome'], end=' ')
print()

print('Lista de pessoas que estão com a idade acima da média: ', end='')
for k in galera:
    if k['idade'] > (soma/len(galera)):
        print(k['nome'], end=' ')
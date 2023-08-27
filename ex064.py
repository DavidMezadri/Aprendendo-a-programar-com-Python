v = 0
z = 0
n = 0
while n != 999:
    print('Digite um número inteiro aleatório ou \n999 - para sair e obter o resultado')
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        z += n
        v += 1
print('A soma de todos os números digitados foi: {}'.format(z))
print('Foram digitados {} números!'.format(v))
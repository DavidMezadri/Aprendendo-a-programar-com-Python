#Nome com todas letras maiúsculas e minúsculas
#quantas letras possui sem o espaços
#quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('Função com replace: {}'.format(len(nome.replace(' ',''))))
print('Função com count: {}'.format(len(nome) - nome.count(' ')))
print('Primeiro com find: {}'.format(nome.find(' ')))
nome = nome.split()
print('Primeiro com split e len: {}'.format(len(nome[0])))

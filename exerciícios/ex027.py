nome = input('Digite teu nome: ').strip()
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[len(nome.split())-1])) #contei quanto
print('Último nome: {}'.format(nome.split()[-1])) #o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante
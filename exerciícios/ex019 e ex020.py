from random import choice, sample
p1 = input('Digite o nome do primeiro participante: ')
p2 = input('Digite o nome do segundo participante: ')
p3 = input('Digite o nome do terceiro participante: ')
p4 = input('Digite o nome do quarto participante: ')

print('O ganhador é {}'.format(choice([p1, p2, p3, p4])))
print('A lista de apresentação segue: {}'.format(sample([p1, p2, p3, p4], k=4)))


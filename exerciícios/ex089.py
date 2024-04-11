alunos = []
a = ''
while True:
    aluno = []
    aluno.append(input('Nome: '))
    aluno.append(int(input('Nota 1: ')))
    aluno.append(int(input('Nota 2: ')))
    a = input('Deseja continuar: [S/N]')
    alunos.append(aluno)
    if a in 'Nn':
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>11}')
print('-'*25)
for i in range(0, len(alunos)):
    print(f'{i:<4}{alunos[i][0]:<10}{(alunos[i][1]+alunos[i][2])/2:>9}')

while a != 999:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if a != 999:
        print(f'Notas de {alunos[a][0]} são [{alunos[a][1]}, {alunos[a][2]}]')

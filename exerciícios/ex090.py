lista = []
while True:
    alunos = {}
    alunos["Nome"] = input('Nome: ')
    alunos["Média"] = float(input(f'Média de {alunos["Nome"]}: '))
    if alunos["Média"] >= 7:
        alunos["Situação"] = 'Aprovado'
    elif 5 <= alunos["Média"] < 7:
        alunos["Situação"] = 'Recuperação'
    else:
        alunos["Situação"] = 'Reprovado'
    lista.append(alunos)
    choice = input('Continuar? [S/N] ')
    if choice in 'nN':
        break
print(lista)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')

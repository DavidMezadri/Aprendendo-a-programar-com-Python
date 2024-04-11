podeserpreso = campari = rapariga = 0
while True:

    sexo = input('Digite o sexo: \nM - Masculino\nF - Feminino\n').lower().strip()
    while sexo not in ['m','f']:
        sexo = input('Digite o sexo: \nM - Masculino\nF - Feminino\n').lower().strip()

    idade = input('Digite o idade:')
    while not idade.isnumeric():
        idade = input('Erro! Digite o idade: ')
    idade = int(idade)
    if idade >= 18:
        podeserpreso += 1
    if sexo == 'm':
        campari += 1
    if sexo == 'f' and idade < 20:
        rapariga += 1

    choice = input('Deseja continuar: \nS - Sim\nN - Não\n').lower()
    while choice not in 'sn':
        choice = input('Erro! Deseja continuar: \nS - Sim\nN - Não\n').lower()
    if choice != 's':
        break
print(f'Pessoas com mais de 18 anos: {podeserpreso}')
print(f'Quantos homens: {campari}')
print(f'Mulheres com mais de 20 anos: {rapariga}')

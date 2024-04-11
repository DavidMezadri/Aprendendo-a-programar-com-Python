pessoa = dict()
from datetime import date
anoatual = date.today().year
pessoa['Nome'] = input('Nome: ')
pessoa['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho: '))
if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = int(input('Salário: '))
print(pessoa)
for j, k in pessoa.items():
    if j == 'Ano de Nascimento':
        print(f'Idade tem o valor {anoatual-pessoa["Ano de Nascimento"]}')
    else:
        print(f'{j} tem o valor {k}')
    if j == 'Ano de Contratação':
           print(f'Aposentadoria no valor {(35 + (anoatual - pessoa["Ano de Contratação"]))+ anoatual - pessoa["Ano de Nascimento"]}') 

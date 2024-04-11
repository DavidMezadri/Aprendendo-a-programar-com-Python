# Dicionários

dados = list()

dados.append('Pedro')
dados.append(25)
print(dados)
# tuplas ()
# listas []
# dicionários {}
dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
#inserir novo intem
dados['sexo'] = 'M'
del dados ['idade']
filme = {
    'titulo':'StarWars',
    'ano':1977,
    'diretor':'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} o {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

brasil = []
estado1 = {'UF': 'Rio der Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['UF'])

estado = dict()
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa '))
    estado['sigla'] = str(input('Sigla do Estado '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:           # Percorre toda a lista com dicionarios dentro
    for k, v in e.items(): # Percorre todos os itens dentro do dicionario
        print(f'O campo {k} tem valor {v}')


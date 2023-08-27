tabela = {'nome': [], 'sexo': [], 'idade': []}
velho = []
hvelho = []
indices = []
mvelha = []
for c in range(0, 4):
    print('Digite os dados da {} pessoa'.format(c+1))
    nome = (input('Digite o nome: '))
    tabela['nome'].append(nome)
    sexo = int(input('Digite o gênero:\n1 - Masculino\n2 - Feminino\n'))
    tabela['sexo'].append(sexo)
    idade = int(input('Digite a idade: '))
    tabela['idade'].append(idade)
# media da idade somando todas e dividindo por len que conta numero de elementos na lista
print('A média de da idade das pesoas é: {} anos'.format((sum(tabela['idade'])/len(tabela['idade']))))

#fazer uma lista com os indices dos homens e tambem suas idades em outra lista
for d in range (0, 4):
    if tabela['sexo'][d] == 1:
        print(type(d))
        hvelho.append(d)
        indices.append(tabela['idade'][d])
print(hvelho)
print(indices)

# percorre a lista de indices e compara todas as idades com a maior dos homens
for e in hvelho:
    if tabela['idade'][e] == max(indices):
            velho.append(tabela['nome'][e])
print('Lista do(s) homem(s) mais velho(s) com {} anos:'.format(max(indices)), velho)

#compara quais são mulheres e se são maiores de 20 anos
for c in range(0, 4):
    if tabela['sexo'][c] == 2 and tabela['idade'][c] >= 20:
        mvelha.append(tabela['nome'][c])
print('Lista da(s) mulheres(s) com mais de 20 anos:', mvelha)

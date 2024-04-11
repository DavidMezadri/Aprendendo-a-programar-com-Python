pessoas = list()
pe = []
lista = ['Joao', 29]
lista1 = ['Maria', 20]
lista2 = ['Pedro', 21]
pe.append(lista+lista1+lista2)
pessoas.append(lista)
pessoas.append(lista1)
pessoas.append(lista2)
print(pessoas)
print(pessoas[0][0][0])
print(pe)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # o [:] é para criarmos uma cópia e nao termos ligação
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
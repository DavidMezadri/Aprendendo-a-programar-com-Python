#Tuplas são caracterizadas por parenteses
#Variáveis compostas
#Tuplas são imutáveis - Definiu a tupla, nao se consegue mudare copm o programa em execução

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

#Nao precisa da posiçào
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')


for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print(lanche)
#ORGANIZADO - nao mudamos a configuração da tupla, mas so mostramos em ordem
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
#tupla é imutável então estamos concatenando
c = b + a
print(c)
print(len(c))
print(c.count(5))#conta quantos do elemento existem dentro da tupla
print(c.index(8))# index mostra em que posição estao elemento, primeira psoição 
print(c.index(2, 4))# desta forma procuramos o 2 a partir do indice 4
frase = 'Curso em Vídeo Python'
#Fatiamento
print(frase[9])
#o último o python não conta, um a menos no final
print(frase[9:21])
#pulando de dois em dois
print(frase[9:21:2])
# quando nao temos número
print(frase[:5])
print(frase[15:])
#Análise da string
print(len(frase)) #Contar quantos caracteres
print(frase.count('o')) #vai contar quantas vezes aparece a letra 'o'. diferencia-se por minúsculo
print(frase.count('o',0, 13))
print(frase.find('deo')) # find mostra onde começa
print('Curso' in frase)

#Transformação
print(frase.replace('Python','Android'))
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
outrafrase = '   Aprenda Python  '
print(outrafrase.strip()) #retirar espaços
print(outrafrase.rstrip()) #retirar espaços a direita
print(outrafrase.lstrip()) #retirar espaços a esquerda

#Divisão
frase = (frase.split()) #Split vai usar os espaços para dividir uma string em uma lista
#string.split(separator, maxsplit)
#Em que:
#string: corresponde ao nome da variável que servirá de base para a divisão;
#separator: indica o caractere utilizado como separador da string;
#maxsplit: representa a quantidade máxima de divisões realizadas.
print(frase)
#Juntar
frase = '-'.join(frase)
print(frase)

print('''Criada em 1991 por Guido van Rossum, um programador
holandês 🇳🇱, a linguagem foi desenvolvida com o objetivo
de ser fácil de aprender e de usar. A origem do nome 
Python vem do programa de televisão Monty Python's Flying
Circus, que era popular entre os programadores da época.''')

frase = frase.replace('-',' ')
print(frase)
dividida = frase.split() #transformei a frase em uma lista
print(dividida[2][2]) # terceira letra da terceira palavra da lista
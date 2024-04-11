frase = input('Escreva uma frase: ').strip()
print("""A sua frase repete {} vezes a letra 'a'.""".format(frase.lower().count('a')))
print(""""A primeira letra 'a' é a {}° letra desta frase""".format(frase.lower().find('a')+1)) #somei +1 pq sempre c omeça no 0
print(""""A última letra 'a' é a {}° letra desta frase""".format(frase.lower().rfind('a')+1))
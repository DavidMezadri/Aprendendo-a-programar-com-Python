#Palindrome
f = input('Digite a frase e descobra se é um palindromo: ')
a = f
a = a.replace(' ', '')
b = ''
print(a)
for c in range(0, len(a)):
    b = a[c] + b

if b == a:
    print(""""A frase '{}' é um palíndromo!""".format(f))
else:
    print(""""A frase '{}' não é um palíndromo!""".format(f))
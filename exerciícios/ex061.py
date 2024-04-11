n = int(input('Digite um número para começarmos a PA: '))
p = int(input('Digite um número da PA: '))
k = n+(p*9)
print(n)
while n != k:
    n += p
    print(n)
print('Fim!!!')
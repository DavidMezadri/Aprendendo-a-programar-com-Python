n = int(input('Digite um número para começarmos a PA: '))
p = int(input('Digite um número da PA: '))
k = 9
print(n)
while k != 0:
    n += p
    k -= 1
    print(n)
    if k == 0:
        k = int(input('Quantos termos deseja ver a mais na PA: '))
print('Fim!!!')
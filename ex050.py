d = 0
e = ''
n = int(input('Digite um número para soma: '))
for c in range(0, 5):
    if n%2 == 0:
        d = d+n
        e = e + ' ' +str(n)
        n = int(input('Digite outro número para soma: '))
    else:
        n = int(input('Digite outro número para soma: '))

e = e.strip()
print("A  soma dos números pares {} é: {}".format(e, d))
l = []
m = 0
v = 0
n = 0
while n != 2:
    a = int(input('Digite um número inteiro: '))
    l.append(a)
    m += a
    v = v + 1
    n = int(input('1 - Digitar mais um número\n2 - Para sair e bter o resultado\n'))
print('O maior número digitado foi: {}'.format(max(l)))
print('O menor número digitado foi: {}'.format(min(l)))
print('A média dos números digitados foi: {}'.format(m/v))

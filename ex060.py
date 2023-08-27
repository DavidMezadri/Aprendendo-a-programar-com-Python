n = int(input('Digite um número para caucularmos o seu fatorial: '))
a = str(n)+'! = '+str(n)
f = 1
while n > 1:
    f *= n
    n -=1
    a += 'x' + str(n)
print(a, '=', f)

# com for
g = int(input('Digite um número para caucularmos o seu fatorial: '))
b = str(g) + '! = ' + str(g)
fatorial = 1
for c in range(g, 0, -1):
    fatorial *= c
    if c != g:
        b += 'x' + str(c)
print(b, '=', fatorial)
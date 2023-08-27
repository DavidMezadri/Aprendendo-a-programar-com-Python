c = f = n = 0
while True:
    f += n
    n = int(input('Digite um número ou 999 para parar!'))
    if n == 999:
        break
    c += 1


print(f'A soma dos {c} digitados resulta em {f}')

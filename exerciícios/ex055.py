l = []
for c in range(0, 5):
    p = int(input('Digite o peso em kg: '))
    l.append(p)
print('O maior peso é: {}'.format(max(l)))
print('O menor peso é: {}'.format(min(l)))
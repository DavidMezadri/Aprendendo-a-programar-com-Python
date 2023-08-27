n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+= n
print('A soma vale{}'.format(s))

n = 'josé'
print(f'O nome dele é {n:-^20}')
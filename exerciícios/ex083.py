a = input('Digite uma expressão para conferência dos parênteses: ')
aberto = []
fechado = [] 
n = 0

for r, i in enumerate(a):
    if n < 0:
        print('A tabulação com parenteses está errada!')
        break
    if i == '(':
        n += 1
        aberto.append(r)
    if i == ')':
        n -= 1
        fechado.append(aberto[-1])
        fechado.append(r)
        aberto.pop()

if n != 0:
    print('A tabulação com parenteses está errada!')
if n == 0:
    print('A tabulação com parenteses esta correta!')
    print(fechado) #mostar as respectivas posiçoes de cada parateses casado dentro da string

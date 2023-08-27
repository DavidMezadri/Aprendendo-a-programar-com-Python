#Método do DAVID

n = int(input('Digite a quantidade elementos da sequencia de fibonacci deseja ver: '))
a = 0
b = 0
c = 0

while n != 0:
    c = a
    a += b
    print(a)
    if a == 0:
        a = 1
        print(a)
    b = c
    n -= 1

#Método do JC

n = int(input('valor '))

a = b = 0

while n != 0:
  print('aqui somado',a)
  if a == 0:
    a = 1
    print(a)
  a += b
  b = a - b
  n -= 1
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
n = 0
while True:
    n = int(input('Digite um número para obter sua tabuada ou número negativo para parar: '))
    if n < 0:
        break
    a = int(input('Digite quantos valores da tabuada do valor deseja: '))
    for c in range(0, a+1):
        print(f'{c} X {n} = {c*n}')
    print('Programa reinciado!')
print('Programa fechado!')
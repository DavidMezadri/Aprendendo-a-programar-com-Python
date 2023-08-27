d = int(input('Digite quantos quilômetros tem sua viagem: '))
if d <= 200:
    print('O preço da sua passagem é: R${}'.format(d*0.5))
else:
    print('O preço da sua passagem é: R${}'.format(d*0.45))
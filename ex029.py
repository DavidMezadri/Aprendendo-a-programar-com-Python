v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado em R${} reias!'.format((v-80)*7))
else:
    print('Parabéns! Você nao foi multado.')

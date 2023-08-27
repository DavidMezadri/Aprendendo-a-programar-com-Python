#Com string
number = str(input('Digite um número entre 0 e 9999: '))
number1=f'{number:0>4}' #mando o programa ter 4 casas e preencher com 0 as casas vazias. Então se o número é 23 ele fica 0023
print('Unidade: {}'.format(number1[3]))
print('Dezena: {}'.format(number1[2]))
print('Centena: {}'.format(number1[1]))
print('Milhar: {}'.format(number1[0]))

#Com matemática meu método
number2 = float(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(number2 % 10))
print('Dezena: {}'.format(((number2 % 100)-(number2 % 10))/10))
print('Centena: {}'.format(((number2 % 1000 - number2 % 100)/100)))
print('Milhar: {}'.format((number2 % 10000 - number2 % 1000)/1000))
#Com matemática com método do guanabara
number2 = float(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(number2 // 1 % 10))
print('Dezena: {}'.format(number2 // 10 % 10))
print('Centena: {}'.format(number2 // 100 % 10))
print('Milhar: {}'.format(number2 // 1000 % 10))

valorsaque = int(input('Qual o valor que deseja sacar: '))
v = valorsaque
notas50 = valorsaque // 50
valorsaque -= 50*notas50

notas20 = valorsaque // 20
valorsaque -= 20*notas20

notas10 = valorsaque // 10
valorsaque =- 10*notas10

notas1 = valorsaque // 1
valorsaque = valorsaque - 1 * notas1

print(f'Você receberá:\n{notas50} notas de 50\n{notas20} notas de 20\n{notas10} notas de 10\n{notas1} notas de 1')



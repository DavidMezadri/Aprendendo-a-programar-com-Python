#carro.siga()
#""objeto.comando""
#carro.esquerda()
#carro.siga()
#carro.direita()
#carro.siga()
#carro.direita()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.pare()

#se carro.esquerda()        if carro.esquerda():
    #bloco_v_               bloco True
#senão                      else:
#bloco_f_                   bloco False
#nunca serõ executados dois blocas nessa situção

tempo = int(input('Quantos anops tem seu carro? '))
if tempo <=3:
    print('Seu carro está novo')
else:
    print('Seu carro está velho')
print('--FIM--')

tempo = int(input('Quantos anops tem seu carro? '))
print('Carro novo'if tempo<=3 else 'Carro velho')
print('--FIM--')

nome = str(input('Qual seu nome? '))
if nome == 'David':
    print('Que nome lindo {}'.format(nome))
else:
    nome == 'Maria'
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))


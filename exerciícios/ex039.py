from datetime import datetime
hoje = datetime.today()
data_nascimento = (input('Digite a data de nascimento: '))
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y') #.strftime('%d/%m/%Y') - transfomar em estring
if data_nascimento <= 5844:
    print('Você ainda vai ter que realizar o alistamento daqui {} dias'.format(data_nascimento-5844))
elif data_nascimento <= 6574:
    print('Você esta hapto a realizar o alistamento,restam {} dias'.format(data_nascimento - 6574))
else:
    print('Você já deve ter rtealizado alistamento, caso não, procure realizar imediatamente')

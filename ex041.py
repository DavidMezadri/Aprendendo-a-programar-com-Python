from datetime import datetime, timedelta
#input da data
age = input(('Digite sua data de nascimento no formato (dd/mm/aaaa) '))
#transformar a data str em data pro sistema
age = (datetime.today() - datetime.strptime(age, '%d/%m/%Y'))/timedelta(days=365)

if age < 9:
    print('Mirim')
elif age < 14:
    print('Infantil')
elif age < 19:
    print('Júnior')
elif age < 20:
    print('Sênior')
elif age >= 20:
    print('Master')
else:
    print('Digite algo válido!')

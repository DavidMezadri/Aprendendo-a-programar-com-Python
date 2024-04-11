from datetime import datetime, timedelta
e = 0
f = 0
for c in range(0, 7):
    d = input('Digite a data de seu nascimento (dd/mm/aaaa): ')
    d = datetime.strptime(d, '%d/%m/%Y')
    d = datetime.today() - d
    if timedelta(days=18*365) < d: #dias com 18 anos
        e = e + 1
    else:
        f = f+1
print('{} pessoas já atingiram a maior idade!'.format(e))
print('{} pessoas não atingiram a maior idade!'.format(f))

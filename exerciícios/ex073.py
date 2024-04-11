times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco da Gama', 'Coritiba', 'América-MG')
#for i in range(0, 5):
    #print(times[i])
#for i in range (len(times)-5, len(times)):
    #print(times[i])

#print(sorted(times))

time = 'Vasco da Gama'

for pos , i in enumerate(times):
    if i == 'Vasco da Gama':
        print(f'O time {i} está na {pos+1} posição.')
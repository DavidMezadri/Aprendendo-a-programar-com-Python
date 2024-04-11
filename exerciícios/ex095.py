user = dict()
gols = list()
jogadores = list()

while True:
    gols.clear()
    user['nome'] = (str(input('Digite o nome do jogador: ')))

    j = int(input(f'Quantas partidas {user["nome"]} jogou? ')) # NAO ESQUECER ASPAS DUPLAS BURRO

    for i in range (0, j):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))

    user['gols'] = gols[:]
    user['total'] = sum(gols)

    jogadores.append(user.copy()) # nao esquecer o parenteses depois de uma função CAVALO!!!!

    while True:
        escolha = str(input('Deseja continuar cadastrando jogadores? [S/N] ')).upper()
        if escolha == 'N' or escolha == 'S':
            break
        print('ERRO! Digite algo válido!')
    if escolha == 'N':
        break

print('')
for i in jogadores:
    print(f'{"cod":<15}', end='')
    for k in i.keys():
        print(f'{k:<15}', end='')
    print('')
    break
    
print(30*'-=')

for w, i in enumerate(jogadores):
    print(f'{w:<15}', end='')
    for j, k in i.items():
        w = len(str(k))
        print(f'{str(k):<15}', end='')
        if j == 'total':
            print('')

print('')

jogador = ''
jogadorexiste = 0

while True:
    jogador = str(input('Mostar dados de qual jogador? (999 para parar) '))
    if jogador == '999':
        break
    for r in jogadores:
        if r['nome'] == jogador:
            jogadorexiste = 1
            print(f'-- LEVANTAMENTO DO JOGADOR {jogador}')
            for jogos, t in enumerate(r['gols']):
                  print(f'   No jogo {jogos+1} fez {t} gols.')
              
    if jogadorexiste == 0:
        print('ERRO! Digite algo válido!!')
    jogadorexiste = 0

print('Obrigado! Volte Sempre!!!')

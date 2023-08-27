import emoji
import random
import time
mao = int(input('Escolha uma opção no Jokenpo:\n1 - {} Pedra\n2 - {} Papel\n3 - {} Tesoura\n'.format(emoji.emojize(':raised_fist:'), emoji.emojize(':raised_hand:'), emoji.emojize(':victory_hand:'))))

pc = random.choice([1, 2, 3])
emojis = ["",emoji.emojize(':raised_fist:'),  emoji.emojize(':raised_hand:'), emoji.emojize(':victory_hand:')]
nomes = ['', 'Pedra', 'Papel', 'Tesoura']


if mao == pc:
    print('Empate!: {} {} empata com {} {}'.format(emojis[mao], nomes[mao], emojis[pc], nomes[pc]))
elif mao == 1 and pc == 3: #pedra ganha de tesoura
    print('Você Venceu!: {} {} vence {} {}'.format(emojis[mao], nomes[mao], emojis[pc], nomes[pc]))
elif mao == 2 and pc == 1:#papel ganha de pedra
    print('Você Venceu!: {} {} vence {} {}'.format(emojis[mao], nomes[mao], emojis[pc], nomes[pc]))
elif mao == 3 and pc == 2:#tesoura ganha de papel
    print('Você Venceu!: {} {} vence {} {}'.format(emojis[mao], nomes[mao], emojis[pc], nomes[pc]))
else:
    print('Você Perdeu!: {} {} perde para {} {}'.format(emojis[mao], nomes[mao], emojis[pc], nomes[pc]))
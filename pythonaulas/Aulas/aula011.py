# Padrão ANSI - Começa com \033[m
# primeriro coódigo 'STYLE', 'TEXT', 'BACK'
# EXEMPLO: \033[0:33:44m
# STYLE:0 - none, 1 - bold, 4 - underline, 7 - negative
# TEXT - 30 - black, 31 - red, 32 - green, 33 - yellow, 34 - blue, 35 - magenta, 36 - cyan, 37 - grey, 97 - white
# BACK - 40 - black, 41 - red, 42 - green, 43 - yellow, 44 - blue, 45 - magenta, 46 - cyan, 47 - grey, 107 - white


print('\033[0;97;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[0;97;42mTeste')
print('\033[mTeste')
print('\033[7;97mTeste\033[m')

nome = 'David'
#isso é um dicionário
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebraco':'\033[7;109m'}
print('Olá, muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebraco'], nome, cores['limpa']))

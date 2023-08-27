c = 0
while c != 5:
    n1 = float(input('Digite um número:'))
    n2 = float(input('Digite outro número:'))
    operacao = int(input('Digite a operação que deseja fazer:\n[1] - Somar\n[2] - Multiplcar\n[3] - Qual o maior\n[4] - Digitar novos números\n[5] - Sair do programa\n'))
    if operacao == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
    if operacao == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, n1*n2))
    if operacao == 3:
        if n1 != n2:
            print('{} é maior que {}'.format(max(n1, n2),min(n1, n2)))
        elif n1 == n2:
            print('{} é igual a {}'.format(n1, n2))
    if operacao == 4:
        print('Digite novos números!')
    if operacao == 5:
        print('Encerrando programa!')
        c = 5

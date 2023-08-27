c = 1
while c == 1:
    sexo = input('Digite seu sexo (M/F): ')
    if sexo.lower() == 'm':
        print(sexo)
        c = 0
    elif sexo.lower() == 'f':
        print(sexo)
        c = 0
    else:
        print('Opção inválida!')
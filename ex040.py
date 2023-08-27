n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nm = (n1+n2)/2
if nm < 5:
    print('Você está reprovado!')
elif nm < 6.9:
    print('Você está de recuperação!')
elif nm >= 7:
    print('Você está aprovado, parabéns!')
else:
    print('Digite algo válido!')
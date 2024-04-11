numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
a = int(input('Digite um número de 0 até 20: '))
while a > 20 or a < 0:
    a = int(input('Error! Digite um número de 0 até 20: '))
print(numeros[a])


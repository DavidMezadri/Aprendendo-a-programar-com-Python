#EXERCICIO 71 BY ENA
def contar_notas(valor):
    notas = [50, 20, 10, 5, 2, 1]
    num_notas = len(notas)

    print(f"Para o valor {valor}, as notas necessárias são:")

    for i in range(num_notas):
        qtd_notas = valor // notas[i]
        if qtd_notas > 0:
            print(f"{qtd_notas} nota(s) de {notas[i]}")
            valor %= notas[i]

valor_digitado = int(input("Digite o valor: "))
contar_notas(valor_digitado)
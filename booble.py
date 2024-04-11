vetor = [25, 65, 2, 4, 12]

for i in range(len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[j] < vetor[i]:
            temp = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = temp
            

            #troca1 = vetor[i]
            #troca2 = vetor[j]
            #vetor[i] = troca2
            #vetor[j] = troca1

print(vetor)



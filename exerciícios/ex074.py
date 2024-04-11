from random import randint
    
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numero sorteados são: {t}\nO maior número é {max(t)}.\nO menor número é {min(t)}.')

from random import randint
from time import sleep
computador = randint(1, 10)
acertou = False
c = 0
print('Pensando em um número')
sleep(1)
print('.', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('.')
sleep(0.5)
while not acertou:
    v = int(input('Em qual número eu pensei entre 1 e 10: '))
    c += 1
    if v == computador:
        acertou = True
    else:
        if v > computador:
            print('muito alto, tente um número menor.')
        elif v < computador:
            print('Muito baixo, tente um número maior.')
print('''Parabéns você acertou!!! 
Total de tentativas: {}'''.format(c))

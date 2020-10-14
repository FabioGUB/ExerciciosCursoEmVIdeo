from random import randint
from time import sleep
print('Irei pensar em um número entre 0 e 5, tente adivinhar qual é')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('Pensando em um número...')
sleep(3)
print('Já sei!!!')
sleep(1.5)
y = randint(0,5)

x = int(input('Em qual número você acha que eu pensei? '))
if y == x:
    print('Parabéns você acertou.')
else:
    print('\033[33mInfelizmente você errou.\033[m Eu pensei no número {}'.format(y))
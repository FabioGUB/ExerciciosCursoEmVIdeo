import random

a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem escolhida foi {}'.format(lista))
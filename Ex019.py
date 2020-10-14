from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
lista = [a, b, c, d]
r = choice(lista)
print ('Quem apagara o quadro será {}.'.format(r))
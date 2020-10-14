x = float(input('Digite o primeiro valor: '))
y = float(input('Digite o segundo valor: '))
z = float(input('Digite o terceiro valor: '))
"""if x > y > z:
    print('O maior valor é {} e o menor é {}'.format(x, z))
if x > z > y:
    print('O maior valor é {} e o menor {}'.format(x, y))"""
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
print('O Maior número é {} e o menor é {}.'.format(maior, menor))

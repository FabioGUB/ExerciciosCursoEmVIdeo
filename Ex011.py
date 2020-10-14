x = float(input('Qual a largura de sua parede? '))
y = float(input('Qual a altura de sua parede? '))
z = (x * y) / 2
print('Para pintar {} m² é necessário {} litros de tinta'.format(x * y, z))

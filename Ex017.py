import math
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h = (ca ** 2 + co ** 2) ** (1 / 2)
print('O valor da hipotenusa é igual a {:.2f}'.format(h))
#ou tambem
hi = math.hypot(co, ca)
print('O valor da hipotenusa é igual a {:.2f}'.format(hi))
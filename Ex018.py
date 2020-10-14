import math
y = float(input('Qual o valor de ângulo: '))
x = math.radians(y)
sen = math.sin(x)
cos = math.cos(x)
tan = math.tan(x)
print('O valor de sen, cos e tg são respectivamente {:.2f}, {:.2f} e {:.2f}.'.format(sen, cos, tan))

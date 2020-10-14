print('__--__' * 5)
print('Analisador de triângulos'.upper())
print('__--__' * 5)
a = float(input('Valor do primeiro segmento: '))
b = float(input('Valor do segundo segmento: '))
c = float(input('Valor do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')


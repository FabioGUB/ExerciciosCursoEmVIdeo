a = float(input('Valor do primeiro segmento: '))
b = float(input('Valor do segundo segmento: '))
c = float(input('Valor do terceiro segmento: '))
if a == b and b == c:
    print('É possível formar um triângulo e ele será um triângulo Equilátero')
elif a < b + c and b < a + c and c < a + b and a == b or b == c or a == c:
    print('É possível formar um triângulo e ele será Isósceles')
elif a < b + c and b < a + c and c < a + b and a != b and b != c and a != c:
    print('É possível formar um triângulo e ele será do formato Escaleno.')
else:
    print('Não é possível formar um triângulo')

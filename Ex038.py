x = int(input('Digite um valor inteiro: '))
y = int(input('Digite outro valor inteiro: '))
if x > y:
    print('{} é maior que {}.'.format(x, y))
elif x < y:
    print('{} é maior que {}.'.format(y, x))
else:
    print('Ambos são iguais.'.format(x, y))

from datetime import date
x = int(input('Qual o ano você deseja analisar? Caso deseje analisar o ano atual digite -1. '))
if x == -1:
    x = date.today().year
y = x % 4
z = x % 100
if y == 0 and z != 0 or x % 400 == 0:
    print('O ano de {} é bissexto.'.format(x))
else:
    print('O ano de {} NÃO é bissexto'.format(x))
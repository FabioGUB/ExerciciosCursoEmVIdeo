from datetime import date
a = int(input('Em qual ano você nasceu? '))
h = date.today().year
f = h - a
if f > 18:
    x = f - 18
    fu = h - x
    print('Você deveria ter se alistado a {} ano(s) atrás em {}.'.format(x, fu))
elif f < 18:
    x = 18 - f
    fu = h + x
    print('Você devera se alistar daqui a {} anos, exatamente no ano de {}.'.format(x, fu))
else:
    print('Você deve se apresentar esse ano para se alistar')

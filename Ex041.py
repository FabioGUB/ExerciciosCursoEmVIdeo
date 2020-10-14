from datetime import date
a = int(input('Em qual ano você nasceu? '))
h = date.today().year - a
if h <= 9:
    print('Você possui {} anos de idade e se encaixa na categoria mirim.'.format(h))
elif h <= 14:
    print('Você possui {} anos de idade e se encaixa na categoria infantil.'.format(h))
elif h <= 19:
    print('Você possui {} anos de idade e se encaixa na categoria junior'.format(h))
elif h <= 20:
    print('Você possui {} anos de idade e se encaixa na categoria se sênior'.format(h))
else:
    print('Você possui {} anos de idade e se encaixa na categoria master'.format(h))

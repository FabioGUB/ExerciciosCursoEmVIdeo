from datetime import date
n = 0
m = 0
for c in range(1,8):
    x = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    h = date.today().year
    if h - x < 18:
        n += 1
    else:
        m += 1
print('{} pessoas são de maior e {} são de menor'.format(m, n))

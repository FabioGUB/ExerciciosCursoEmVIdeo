y = int(input('Digite um número: '))
u = y // 1 % 10
d = y // 10 % 10
c = y // 100 % 10
m = y // 1000 % 10
print('Analisando o número {}'.format(y))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

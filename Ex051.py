print('=+=' * 8)
print('10 primeiros termos de uma P.A'.upper())
print('=+=' * 8)

x = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
d = x + (10 - 1) * r
for c in range(x, d + 1 , r):
    print(c, end=' -> ')
print('...')

print('Gerador de P.A')
p = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
i = 0
print(p, end='')
while i < 9:
    p += r
    print(' ->', p, end='')
    i += 1
print('...')

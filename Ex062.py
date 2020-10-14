print('Gerador de P.A 3.0')
p = int(input('Primeiro da P.A: '))
r = int(input('Razão da P.A: '))
i = 1
n = 0
m = 10
print(p, end='')
while m != 0:
    n = n + m
    while i < n:
        p += r
        print(' ->', p, end='')
        i += 1
    print('... PAUSA')
    m = int(input('Quantos termos a mais você deseja? '))
print('FIM da progressão sendo mostradas {} termos.'.format(n))

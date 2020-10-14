print('Sequência de Fibonacci')
x = int(input('Quantos termos você deseja mostrar? '))
t0 = 0
t = 1
i = 3
print('{} -> {}'.format(t0, t), end=' -> ')
while i <= x:
    t3 = t0 + t
    t0 = t
    t = t3
    print(t3, end=' -> ')
    i += 1
print('FIM')

x = int(input('Digite um némero para saber se ele é primo: '))
t = 0
for c in range(1, x + 1):
    if x % c == 0:
        print('\033[35m', end=' ')
        t+=1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vez(es).'.format(x, t))
if t == 2:
    print('É um número primo')
else:
    print('Não é um número primo')

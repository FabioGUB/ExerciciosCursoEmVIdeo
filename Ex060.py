
x = int(input('Qual número você deseja obter o fatorial? '))
i = x
f = 1
while i > 0:
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print('{}'.format(f))




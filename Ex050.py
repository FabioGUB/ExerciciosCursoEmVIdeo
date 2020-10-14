s = 0
c = 1
for c in range(1, 7):
    x = int(input('Insira o {}º valor inteiro: '.format(c)))
    if x % 2 == 0:
        s += x
        c += 1
print('Você informou {} numeros pares e a soma deles resulta em {}.'.format(c, s))

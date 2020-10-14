s = c = m = maior = menor = 0
i = 'S'
while i in 'S':
    x = int(input('Digite um valor: '))
    s += x
    c += 1
    if c == 1:
        menor = maior = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    i = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while i not in 'SsNn':
        print('Insira um valor válido')
        i = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
m = s / c
print('Você digitou {} números e a média foi {}.'.format(c, m))
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))

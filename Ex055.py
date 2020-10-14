maior = 0
menor = 0
for c in range(1,6):
    x = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = x
        menor = x
    else:
        if x >  maior:
            maior = x
        if x < menor:
            menor = x
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é de {}Kg'.format(menor))
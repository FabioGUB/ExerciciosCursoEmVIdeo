x = (int(input('Insira um valor: ')),
    int(input('Insira outro valor: ')),
    int(input('Insira o 3º valor: ')),
    int(input('Insira o 4º valor: ')))
print(f'Você digitou os valores {x}')
if 3 in x:
    print(f'O número 3 apareceu a primeira vez na {x.index (3) + 1}ª posição. ')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
print(f'O número 9 aparaceu {x.count(9)} vez(es).')
print(f'Os números pares são: ',end='')
for n in x:
    if n % 2 == 0:
        print(n, end=' ')

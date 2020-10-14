c = 0
c1 = 0
c2 = 0
while True:
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if i >= 18:
        c += 1
    if s == 'M':
        c1 += 1
    if s == 'F' and i < 20:
        c2 += 1
    f = str(input('deseja continuar? [S/N]')).upper().strip()[0]
    while f not in 'SsNn':
        print('Insira um valor válido.')
        f = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    print('=-' * 20)
    if f == 'N':
        break
print(f'{c} pessoa(s) são maiores de idade.')
print(f'{c1} são homens.')
print(f'{c2} são mulheres com menos de 20 anos')

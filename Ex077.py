x = 'acaso', 'teclado', 'veia', 'receio', 'aleatorio', 'tupla', 'falso', 'verdadeiro', 'vogal', 'time'
for c in x:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for l in c:
        if l in 'aeio':
            print(l, end=' ')

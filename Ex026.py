x = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} vezes na frase.'.format(x.count('A')))
print('A primeira letra "A" está na posição {}.'.format(x.find('A') + 1))
print('A última letra "A" aparece na posição {}.'.format(x.rfind('A') + 1))


f = str(input('Digite uma frase: ')).upper().strip()
p = f.split()
j = ''.join(p)
i = ''
for c in range(len(j) - 1, -1, -1):
    i+=j[c]
if j == i:
    print('É palindromo')
else:
    print('Não é palindromo')

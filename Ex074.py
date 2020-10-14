from random import randint
menor = maior = co = 0
x = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
print(x)
for c in x:
    co += 1
    if co == 1:
        menor = maior = c
    elif menor > c:
        menor = c
    elif maior < c:
        maior = c
print(f'O menor valor é {menor}.')
print(f'O maior valor é {maior}')

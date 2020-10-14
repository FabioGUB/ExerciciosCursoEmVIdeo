listagem = ('Pão', 0.5, 'Café', 2, 'Leite', 3, 'Queijo', 4, 'Laranja', 0.75, 'Danone', 3, 'Refrigerante', 6, 'Esfiha', 2.5,
            'Coxinha', 3)
print('=' * 37)
print(f'{"Lista de preços":^35}')
print('=' * 37)
for n in range(0, len(listagem)):
    if n % 2 == 0:
        print(f'{listagem[n]:.<30}', end='')
    else:
        print(f'R$ {listagem[n]:>2.2f}')
print('=' * 37)

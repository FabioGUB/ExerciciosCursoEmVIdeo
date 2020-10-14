print('LOJA DO BINHAL')
print('-=' * 20)
s = c = c1 = m = 0
b = ''

while True:
    produto = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço do Produto: R$ '))
    s += preco
    c1 += 1
    if preco > 1000:
        c += 1
    if c1 == 1 or preco < m:
        m = preco
        b = produto
    d = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('-=' * 20)
    while d not in 'SN':
        print('Insira um valor válido')
        d = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if d == 'N':
        break
print(f'O valor total dos produtos é de {s:.2f}')
print(f'Total de produtos que custaram mais de R$ 1000.00 = {c}')
print(f'O produto de menor preço foi o(a) {b} custando R$ {m:.2f}')
print('{:-^55}'.format('FIM DO PROGRAMA '))

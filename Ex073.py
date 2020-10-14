tabela = 'Atlético MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco', 'Flamengo', 'Fluminense', 'Botafogo', 'Sport', 'Santos', 'Fortaleza', 'Athletico', 'Ceara', 'Grêmio', 'Corinthians', 'Atlético GO', 'Coritiba', 'Bragantino', 'Goiás', 'Bahia '
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[16:]}')
print(f'''Os times em ordem alfabética são:
{sorted(tabela)}''')
print(f'O time do corinthians está na {tabela.index("Corinthians") + 1}ª posição')


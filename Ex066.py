print('Leitor de Números')
i = s = 0
while True:
    x = int(input('Insira um número inteiro. [999 para parar]:  '))
    if x == 999:
        break
    s += x
    i += 1
print(f'Você digitou {i} números e a soma deles resultam em {s}')

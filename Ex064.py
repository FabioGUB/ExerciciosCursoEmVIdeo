x = s = i = 0
while x != 999:
    x = int(input('Digite um número inteiro, [999] para parar: ' ))
    s += x
    i += 1
print('Você digitou {} numeros que resultam em uma soma de {}'.format(i - 1, s - 999))

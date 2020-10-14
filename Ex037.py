x = int(input('Insira um número inteiro: '))
print('''Para qual base deseja converter? 
[ 1 ] Binário
[ 2 ] Hexadecimal
[ 3 ] Octal''')
y = int(input('Qual a opção desejada? '))

if y == 1:
    print('{} convertido para Binário fica {}.'.format(x, bin(x)[2:]))
elif y == 2:
    print('{} convertido para a base hexadecimal resulta em {}'.format(x, hex(x)[2:]))
elif y == 3:
    print('{} convertido para a base Octal resulta em {}'.format(x, oct(x)[2:]))
else:
    print('Opção inválida, tente novamente')
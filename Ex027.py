x = str(input('Qual seu nome completo: ')).title().strip().split()
print('Seu primeiro nome é: {}'.format(x[0]))
print('Seu último nome é: {}'.format(x[len(x) - 1]))



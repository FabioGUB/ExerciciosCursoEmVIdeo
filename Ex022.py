x = str(input('Qual o seu nome? ')).strip()
print('O seu nome em maiúsculo fica {}'.format(x.upper()))
print('Em minúscula {}'.format(x.lower()))
print('Sem considerar os espeços seu nome possui um total de {} caracteres'.format(len(x) - x.count(' ')))
print('Seu primeiro nome é {} e possui {} letras'.format(x.split()[0], x.find(' ')))
#ou
# separa = x.split()
# print('Seu primeiro  nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))

n = str(input('Qual o seu sexo [F/M]? ')).strip().upper()[0]
while n not in 'FfMm':
    print('Tente novamente')
    n = str(input('Qual o seu sexo [F/M]? ')).strip().upper()[0]
print('Sexo {} registrado'.format(n))
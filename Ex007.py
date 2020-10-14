x = float(input('Nota da primeria prova: '))
y = float(input('Nota da segunda prova: '))
z = (x + y) / 2
if z >= 6:
    print('Parabéns, você foi aprovado com a média de {}'.format(z))
else:
    print('Infelizmente você foi reprovado, estude mais da próxima')

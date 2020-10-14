v = float(input('Qual era velocidade do carro em Km/h? '))

if v > 80:
    print('Você será multado em R${}.'.format((v - 80) * 7))
else:
    print('Parabéns você estava dentro do limite de velocidade!!!')

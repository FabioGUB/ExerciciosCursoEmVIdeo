x = int(input('Qual será a distância da viagem? '))
if x <= 200:
   p = x * 0.50
else:
    p = x * 0.45
print('Você irá pagar R${:.2f} na passagem.'.format(p))

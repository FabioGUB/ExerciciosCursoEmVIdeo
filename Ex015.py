x = float(input('Quantos dias alugado? '))
y = float(input('Quantos km foi rodado? '))
t = (x * 60) + (y * 0.15)
print('O total a pagar é de R$ {}'.format(t))

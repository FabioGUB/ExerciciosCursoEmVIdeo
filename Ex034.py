x = float(input('Qual o salário do funcionário? R$ '))
if x > 1250:
    y = (x * 10 / 100) + x
else:
    y = (x * 15 / 100) + x
print('Seu novo salário será de R${:.2f}.'.format(y))

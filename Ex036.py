print('--_--' * 8)
print('EMPRÉSTIMO BANCÁRIO')
print('--_--' * 8)
x = float(input('Qual o valor da casa? R$'))
y = float(input('Qual o seu salário? R$'))
z = float(input('Em quantos anos deseja pagar a casa? '))
pm = x / (z * 12)
s = y * 30 / 100
print('Com esses valores você teria que pagar prestações de R${:.2f}.'.format(pm))
if pm > s:
    print('\033[32mInfelizmente o empréstimo não foi aprovado')
else:
    print('Parabéns, empréstimo aprovado')

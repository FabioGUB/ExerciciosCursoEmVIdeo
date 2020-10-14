from time import sleep
from random import choice
print('*' * 20)
print('JOGO DA VELHA')
print('*' * 20)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
x = choice(lista)
m = str(input('Pedra, papel ou tesoura? ')).upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print(x)
if x == 'PEDRA' and m == 'PAPEL' or x == 'PAPEL' and m == 'TESOURA' or x == 'TESOURA' and m == 'PEDRA':
    print('Você ganhou')
elif x == 'PAPEL' and m == 'PEDRA' or x == 'TESOURA' and m == 'PAPEL' or x == 'PEDRA' and m == 'TESOURA':
    print('O computador ganhou')
else:
    print('EMPATE')
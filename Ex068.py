from random import randint

print('PAR OU IMPAR')
x = ''
y = 0
i = 0
while True:
    x = str(input('Você quer par ou impar? [P/I] ')).upper().strip()
    while x not in 'IiPp':
        print('Insira um valor válido')
        x = str(input('Você quer par ou impar? [P/I] ')).upper().strip()
    y = int(input('Digite um valor: '))
    computador = randint(0, 10)
    t = y + computador
    if x == 'I' and t % 2 == 0 or x == 'P' and t % 2 == 1:
        print(f'Você escolheu {y} e o computador {computador}, a soma resulta em {t}')
        print('Você perdeu')
        break
    elif x == 'I' and t % 2 == 1 or x == 'P' and t % 2 == 0:
        print(f'Você escolheu {y} e o computador {computador}, a soma resulta em {t}')
        print('Você GANHOU')
        print('Vamos novamente')
    i += 1
print(f'Você ganhou {i} vez(es) consecutivas.')

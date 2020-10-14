from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
f = 0
while f != 5:
    print('=-=' * 20)
    f = int(input('''O que você deseja fazer:
    [ 1 ] para multiplicar os dois números
    [ 2 ] para somar os dois números
    [ 3 ] para mostrar o maior
    [ 4 ] para digitar novos números
    [ 5 ] para finalizar o programa
    Opção desejada: '''))
    if f == 1:
        print('A multiplicação entre {} e {} resulta em {}'.format(n1, n2, n1 * n2))
    elif f == 2:
        print('A soma de {} e {} resulta em {}'.format(n1, n2, n1 + n2))
    elif f == 3:
        if n1 > n2:
            print('O maior valor entre os dois é {}'.format(n1))
        elif n2 > n1:
            print('O maior valor entre os dois é {}'.format(n2))
        else:
            print('Ambos valores são iguais')
    elif f == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro novo valor: '))
    elif f == 5:
        print('Finalizando', end='')
        sleep(0.5)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(0.75)
        print('.')
    else:
        print('Opção Inválida, tente novamente.')
print('Programa finalizado')

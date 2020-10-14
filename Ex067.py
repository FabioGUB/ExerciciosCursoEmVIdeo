print('Tabuada')
i = 0
while True:
    x = int(input('Você deseja ver a tabuada de qual valor? '))
    if x < 0:
        break
    for c in range (1, 11):
        t = x * c
        print(f'{x} x {c} = {t}')

print('Programa Finalizado')

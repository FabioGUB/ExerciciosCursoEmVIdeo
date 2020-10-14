n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
m = (n1 + n2) / 2
if m >= 7.0:
    print('Parabéns você foi aprovado e já pode entrar de férias.')
elif m < 5.0:
    print('Infelizmente você foi reprovado, estude mais.')
else:
    print('Você está de recuperação, se esforce para passar de ano')

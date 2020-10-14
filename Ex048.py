co = 0
s = 0
for c in range(0, 500, 3):
  if c % 2 == 1:
      s = s + c
      co = co + 1
print('A soma dos valores impares multiplos de 3 entre 0 e 500 possui {} termos e resulta em {}.'.format(co, s))
#ou print(sum(range(3, 501, 6)))
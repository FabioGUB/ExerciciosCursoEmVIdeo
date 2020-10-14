x = int(input('Digite um número entre 0 e 20: '))
y = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while x < 0 or x > 20:
    x = int(input('Insira um valor válido entre 0 e 20: '))
z = y[x]
print(f'O valor digitado escrito por extenso é: {z}')

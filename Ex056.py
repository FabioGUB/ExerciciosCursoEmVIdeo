somadasidades = 0  # soma das idades
maioridadehomem = 0  # maior idade masculina
mediaidade = 0  # média das idades
nomemaisvelho = ''  # nome do homem mais velho
mulher20 = 0
for c in range(1, 5):
    print('------ {}ª pessoa ------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somadasidades += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidade = somadasidades / 4
print('A média do grupo foi de {:.1f} anos.'.format(mediaidade))
print('O homem mais velho possui {} anos e o nome dele é {}'.format(maioridadehomem, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))

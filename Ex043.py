print('......' * 4)
print('Calculadora IMC')
print('......' * 4)
peso = float(input('Qual o seu peso? (KG) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / (altura ** 2)
print('IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('SEU IMC ESTÁ ABAIXO DO INDICADO PARA SUA ALTURA E PESO')
elif imc < 25:
    print('SEU IMC ESTÁ NO VALOR IDEAL')
elif imc < 30:
    print('SEU IMC SE ENCONTRA EM UMA TAXA DE SOBREPESO')
elif imc < 40:
    print('DE ACORDO COM SEU IMC VOCÊ EM SE ENCONTRA EM OBESIDADE')
else:
    print('SEU IMC INDICA UMA OBESIDADE MÓRBIDA')

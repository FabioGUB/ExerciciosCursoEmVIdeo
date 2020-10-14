valor = float(input('Qual é o preço atual do produto? '))
print('\033[1mQual será a forma de pagamento?\033[m')
print('''Digite o número de acordo com a forma desejada
[ 1 ] Para pagamentos à vista (dinheiro ou cheque) com 10% de desconto' 
[ 2 ] Para pagamentos à vista (cartão) com 5% de desconto
[ 3 ] Para pagar em até 2x no cartão sem descontos')
[ 4 ] Para pagar em 3x ou mais no cartão com 20% de juros''')
pagamento = int(input('Forma de pagamento escolhida: '))
if pagamento == 1:
    vf = valor - (valor * 10 / 100)
    print('A forma de pagamento selecionada foi pagamento à vista no dinheiro ou cheque com 10% de descontos, '
          'o novo valor do produto será de {}.'.format(vf))
elif pagamento == 2:
    vf = valor - (valor * 5 / 100)
    print('A forma de pagamento selecionada foi á vista no cartão e você terá direito a 5% off, o novo valor do '
          'produto será de {:.2f}.'.format(vf))
elif pagamento == 3:
    vf = valor / 2
    print('A forma de pagamento selecionada foi em até 2x no cartão, assim cada parcela terá o valor de {}.'.format(vf))
elif pagamento == 4:
    vf = valor + (valor * 20 / 100)
    v = int(input('Você escolheu pagar em 3x ou mais. Em quantas vezes você deseja pagar? '))
    f = vf / v
    print('O valor das parcelas será de {:.2f}.'.format(f))
else:
    print('Opção inválida')

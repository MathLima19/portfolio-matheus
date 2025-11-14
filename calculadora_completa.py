n1 = float(input('Digite um n : '))
n2 = float(input( 'Digite outro n : '))
operacao = input('Escolha uma operação ( soma, subtracao, multiplicacao, divisao)').lower()
soma = (n1 + n2)
subtracao = (n1 - n2)
multiplicacao = (n1 * n2)
divisao = (n1 / n2)

if operacao == 'soma':
    print (soma)
elif operacao == 'subtracao:':
    print(subtracao)
elif operacao == 'multiplicacao':
    print(multiplicacao)
else:
    print(divisao)
    
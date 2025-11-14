#Crie um programa que calcule o IMC de uma pessoa. 
# IMC = peso / altura ²

peso = float(input('Qual seu peso ? :'))


altura = float(input('Qual sua altura ?'))
               
imc = peso / altura ** 2 

if imc < 18.5:
    print('Voce está so o osso, abaixo do peso.')
elif imc  <= 18.5 : 
    print('Ta normal.')
elif imc 
                   
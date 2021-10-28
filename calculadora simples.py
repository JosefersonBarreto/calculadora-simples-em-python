# This is a sample Python script.


conta = input('Digite o nome da operação:soma/subtração/multiplicação/divisão =')

if conta== "soma":
    num=int(input('digite um numero:'))
    num2=int(input('digite um numero'))
    somar= num +num2
    print("o resultado é:",somar)

elif conta== "subtração":
    num=int(input('digite um numero:'))
    num2=int(input('digite outro numero'))
    subtrair= num - num2
    print("o valor da subtração é :",subtrair)

elif conta=="multiplicação":
 num=int(input('digite um numero:'))
 num2=int(input('digite um numero :'))
 multiplicacao=num*num2
 print("o resultado da multiplicação é:",multiplicacao)

elif conta=="divisão":
    num=int(input('digite um numero:'))
    num2=int(input('digite outro numero:'))
    divisao=num/num2
    print("o resultado da divisão é:",int(divisao))
else:
    print("lamentamos,ainda estamos implementando outras funcionalidades")
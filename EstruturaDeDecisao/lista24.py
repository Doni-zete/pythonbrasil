numero1 = float(input("Informe um numero: "))
numero2 = float(input("Informe um numero: "))

opcao = input("Informe a operação que deseja realizar [+] [*] [-] [/]: ")


if(opcao == '+'):
    soma = numero1+numero2
    print("Resulado: ", soma)
    if(soma % 2 == 0):
        print("par")
    else:
        print("impar")
    if(soma > 0):
        print("positivo")
    else:
        print("negativo")
    if(soma // 1 == soma):
        print("inteiro")
    else:
        print("decimal")

elif(opcao == '-'):
    subtracao = numero1-numero2
    print("Resulado: ", subtracao)
    if(subtracao % 2 == 0):
        print("par")
    else:
        print("impar")
    if(subtracao > 0):
        print("positivo")
    else:
        print("negativo")
    if(subtracao // 1 == subtracao):
        print("inteiro")
    else:
        print("decimal")

elif(opcao == '*'):
    multipliacaco = numero1*numero2
    print("Resulado: ", multipliacaco)

    if(multipliacaco % 2 == 0):
        print("par")
    else:
        print("impar")
    if(multipliacaco > 0):
        print("positivo")
    else:
        print("negativo")
    if(multipliacaco // 1 == multipliacaco):
        print("inteiro")
    else:
        print("decimal")


elif(opcao == '/'):
    divisao = numero1/numero2
    print("Resulado: ", divisao)
    if(divisao % 2 == 0):
        print("par")
    else:
        print("impar")
    if(divisao > 0):
        print("positivo")
    else:
        print("negativo")
    if(divisao // 1 == divisao):
        print("inteiro")
    else:
        print("decimal")




altura = float(input("Informe sua altura: "))
sexo = str(input("Informe seu sexo [m] masculino ou [f] feminino: "))
if(sexo == "m"):
    calculo = (72.7*altura)-58
else:
    if(sexo == "f"):
        calculo = (62.1*altura)-44.7

print("Seu peso ideal eh: {:.2f}".format(calculo))

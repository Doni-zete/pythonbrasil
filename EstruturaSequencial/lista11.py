numero1 = int(input("Informe um numero inteiro: "))
numero2 = int(input("Informe outro numero inteiro: "))
numero3 = float(input("Informe um numero real: "))

calculo_dobro = (numero1*numero1) + (numero2/2)
calculo_triplo = (numero1*3)+numero3
calculo_elevado = numero3 ** 5

print("Dobro do primeiro com metade do segundo: ", calculo_dobro)
print("Soma do triplo do primeiro com o terceiro: ", calculo_triplo)
print("Terceiro elevado ao cubo: {:.2f} ".format(calculo_elevado))

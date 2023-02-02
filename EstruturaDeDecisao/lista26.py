tipo_combustivel = input(
    "Informe o tipo de combustível, (a-álcool, g-gasolina): ")
litros = float(input("Informe a quantidade de litros: "))

gasolina = 2.50
alcool = 1.90

if(tipo_combustivel == "a" and litros < 20):
    desconto = litros * (0.03)
    resultado = (litros - desconto)
else:

    desconto = litros * (0.05)
    resultado = (litros - desconto)

if(tipo_combustivel == "g" and litros < 20):
    desconto = litros * (0.04)
    resultado = (litros - desconto)*gasolina
else:
    if(litros > 20):
        desconto = litros * (0.06)
        resultado = (litros - desconto)*gasolina

print("Valor a ser pago pelo cliente:R$ {:.2f}".format(resultado))

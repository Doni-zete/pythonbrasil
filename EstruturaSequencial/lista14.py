peso = float(input("Informe o peso do peixe: "))

excedente = 0


if(peso > 50):
    excesso = peso-50
    multa = excesso*4
    print("Peso de peixes", peso,
          "kg maior que o estabelecido que é 50kg multa de R$", multa)
else:
    print("Peso de peixes", peso, "dentro do estabelecido 50kg ")

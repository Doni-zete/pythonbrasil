tabuada = int(input("Informe um numero: "))

print("Tabuada de: ", tabuada)
for item in range(1, 11):
    calculo = tabuada * item
    print(f"{tabuada} x {item} = {calculo} ")

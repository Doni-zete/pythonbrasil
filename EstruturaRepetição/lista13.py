base = int(input("Informe um numero: "))
expoente = int(input("Informe outro numero: "))

pontencia = 1
for item in range(expoente):
    pontencia *= base
    item += 1
    print(f"{base} ^ {expoente} = {pontencia}")

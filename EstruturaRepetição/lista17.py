numero = int(input("Informe um numero: "))


fatorial = 1
for item in range(1, numero + 1):
    fatorial = fatorial*item

    print(f"{numero} != {fatorial}")

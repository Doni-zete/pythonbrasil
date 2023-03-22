num = int(input("Informe um numero: "))
fatorial = 1
for item in range(1, num + 1):
    fatorial = fatorial * item

print(f"O fatorial de {num} é {fatorial}.")

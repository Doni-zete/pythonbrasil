numero_inicial = int(input("Informe um número: "))
numero_final = int(input("Informe um número final: "))


for itemI in range(numero_inicial, numero_final + 1):
    primo = 0

    for itemJ in range(1, itemI + 1):
        if(itemI % itemJ) == 0:
            primo += 1
    if(primo == 2):
        print("O número " + itemI + " é PRIMO!")

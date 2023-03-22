quantidade_temperatuta = int(input("Informe a quantidade de temperatua: "))

lista_tempeatura = []


for item in range(quantidade_temperatuta):
    temperatura = float(input("Informe uma temperarua: "))

    lista_tempeatura.append(temperatura)

    maior_temperatura = lista_tempeatura[0]
    menor_temperatura = lista_tempeatura[0]

    for item in lista_tempeatura:
        if(item > maior_temperatura):
            maior_temperatura = item

        if(item < menor_temperatura):
            menor_temperatura = item

print(maior_temperatura)
print(menor_temperatura)

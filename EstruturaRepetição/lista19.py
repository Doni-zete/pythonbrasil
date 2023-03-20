n = int(input("Informe a quantidade de n numeros: "))
lista_numeros = []
soma = 0

for item in range(n):

    numero = float(input(f"Informe o {item+1}° numero: "))
    while numero <= 0 or numero > 1000:
        print("Digite novamente apenas números entre 0 e 1000: \n")
        numero = float(input(f"Informe o {item+1}° numero: \n"))

    lista_numeros.append(numero)
    soma += numero

maior = lista_numeros[0]
menor = lista_numeros[0]

for item in range(1, len(lista_numeros)):
    if(lista_numeros[item] > maior):
        maior = lista_numeros[item]
    elif(lista_numeros[item] < menor):
        menor = lista_numeros[item]


print(lista_numeros)
print(f"O maior número: {maior} ")
print(f"O menor número: {menor} ")
print(f"A soma dos números: {soma}")

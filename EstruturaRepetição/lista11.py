numero1 = int(input("Informe um numero: "))
numero2 = int(input("Informe outro numero: "))
soma = 0
soma_total = 0

if(numero1 < numero2):
    for item in range(numero1, numero2+1):
        print(item)
        soma += item
else:
    for item in range(numero2, numero1+1):
        print(item)
        soma += item

print("Soma dos numeros: ",soma)

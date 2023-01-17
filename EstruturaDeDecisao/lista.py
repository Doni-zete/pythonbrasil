numero = list(map(int, (input("Informe 3 numero : ").split())))
maior = numero[0]

if(numero[1] > numero[0] and numero[1] > numero[2]):
    maior = numero[1]
if(numero[2] > numero[0] and numero[2] > numero[1]):
    maior = numero[2]

menor = numero[0]
if(numero[1] < numero[0] and numero[1] < numero[2]):
    menor = numero[1]
if(numero[2] < numero[0] and numero[2] < numero[1]):
    menor = numero[2]

print("O maior eh: ", maior)
print("O menor eh ", menor)

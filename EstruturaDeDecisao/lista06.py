numero = list(map(int, (input("Informe 3 numero : ").split())))
maior = numero[0]

if(numero[1] > maior):
    maior = numero[1]
elif(numero[2] > maior):
    maior = numero[2]
    

print("O maior eh: ", maior)

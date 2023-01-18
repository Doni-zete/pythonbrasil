numero1 = int(input("Informe um numero: "))
numero2 = int(input("Informe um numero: "))
numero3 = int(input("Informe um numero: "))


if(numero1 < numero3):
    numero1, numero3 = numero3, numero1

if(numero1 < numero2):
    numero1, numero2 = numero2, numero1

if(numero2 < numero3):
    numero2, numero3 = numero3, numero2

print(f"A ordem decrescente é {numero1},{numero2}, {numero3}")

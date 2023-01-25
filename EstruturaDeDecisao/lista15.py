lado1 = int(input("Informe um lado: "))
lado2 = int(input("Informe um lado: "))
lado3 = int(input("Informe um lado: "))

if(lado1+lado2 < lado3) and (lado2+lado3 < lado1) and (lado3+lado1 < lado2):
    print("Triângulo soma de quaisquer dois lados for maior que o terceiro")

elif(lado1 == lado2) and (lado1 == lado3):
    print("Triângulo Equilátero: três lados iguais")

elif(lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("Triângulo Isósceles: quaisquer dois lados iguais")
else:
    print("Triângulo Escaleno: três lados diferentes")

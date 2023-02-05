numero = list(map(int, (input("Informe 10 numeros com espaço: ").split())))

par = 0
impar = 0
for item in numero:
    if(item % 2 == 0):
        par = par+1
        print("Números par: ",item)
    else:
        impar = impar + 1
        print("Números impar: ",item)
print("Quantidade de números pares: ",par)
print("Quantidade de números impares: ",impar)

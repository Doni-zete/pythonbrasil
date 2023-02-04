letra_vogal = str(input("Informe uma letra: "))

lista_vogal = ["a", "e", "i", "o", "u"]

if(letra_vogal in lista_vogal):
    print("Letra digitada {} é uma vogal: ".format(letra_vogal))

else:
    print("Letra digitada {} é uma consoante: ".format(letra_vogal))

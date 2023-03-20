n_pessoas = int(input("Informe o numero de n pessoas: "))

lista_pessoas = []
media = 0

for item in range(n_pessoas):
    idade = int(input("Informe sua idade: "))
    lista_pessoas.append(idade)

    media += idade/n_pessoas

if(media >= 0 and media <= 25):
    print("Jovem")
elif(media >= 26 and media <= 60):
    print("Adulta")
else:
    print("Idosa")

print(int(media))

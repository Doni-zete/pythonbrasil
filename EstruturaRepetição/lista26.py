numero_eleitores = int(input("Informe o numero de eleitores: "))

lista_eleitores = []

candidato1 = 0
candidato2 = 0
candidato3 = 0


for item in range(numero_eleitores):
    voto = int(input("Informe seu voto [1] ou [2] ou [3]"))

    if(voto == 1):
        candidato1 += 1
    elif(voto == 2):
        candidato2 += 1
    elif(voto == 3):
        candidato3 += 1


print("Votos para o candidato 1: ", candidato1)
print("Votos para o candidato 2: ", candidato2)
print("Votos para o candidato 3: ", candidato3)

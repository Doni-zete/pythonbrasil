print("\tData Válida\n")

# Entrada de dados
data = (input("Data: "))

# Fatiamento e cálculo
if int(data[0:2]) != 0 and int(data[0:2]) <= 31:
    if int(data[3:5]) != 0 and int(data[3:5]) <= 12:
        if int(data[6:11]) != 0:
            print("")
            print("Data Válida")
        else:
            print("")
            print("Data Inválida")
    else:
        print("")
        print("Data Inválida")
else:
    print("")
    print("Data Inválida")

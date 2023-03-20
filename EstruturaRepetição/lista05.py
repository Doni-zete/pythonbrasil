while True:
    A = int(input("Informe a população A: "))
    B = int(input("Informe a população B: "))

    taxaA = float(input("Informe a taxa A: "))
    taxaB = float(input("Informe a taxa B: "))

    anos = 0
    while A < B:
        A = A + (A * (taxaA/100))
        B = B + (B * (taxaB/100))
        anos = anos + 1

    print("Serão necessarios " + str(anos) +
          " anos para que a população do país\n" +
          "A ultrapasse ou iguale a população do país B")

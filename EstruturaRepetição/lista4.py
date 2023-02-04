
A = 80000
B = 200000
taxaA = 0.03
taxaB = 0.015

anos = 0
while A < B:
    A = A + (A * taxaA)
    B = B + (B * taxaB)
    anos = anos + 1

print ("Serão necessarios " + str(anos) + " anos para que a população do país  A ultrapasse ou iguale a população do país B")
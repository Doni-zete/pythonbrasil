preco = list(map(float, input("Informe o preço de três produtos: ").split()))

menor = preco[0]

if(preco[1] < preco[0] and preco[1] <preco[2]):
    menor = preco[1]
if(preco[2] < preco[0] and preco[2] <preco[1]):
    menor = preco[2]

print("Esse produto é o mais barato: ", menor)

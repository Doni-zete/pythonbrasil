print("Preço do pão: R$ 0.18\n \nPanificadora Pão de Ontem")

for item in range(1, 51):
    preco = 0.18*item
    print(item, "- R$ %.2f" % preco)

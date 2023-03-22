numero = 0
valor_compra = 0
troco = 0

while(True):
    numero = float(input("Informe um numero ou digite 0 para sair: "))
    if(numero == 0):
        break
    dinheiro = float(input("Quanto em dinheiro você tem: "))
    print("Total: %.2f" % valor_compra)

    valor_compra += numero

    while(True):
        dinheiro = float(input("Digite novamente valor insuficiente: "))
        if(dinheiro < valor_compra):
            troco = valor_compra - dinheiro
  

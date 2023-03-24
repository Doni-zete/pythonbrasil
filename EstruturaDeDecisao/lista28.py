tipo_Carne = str(input("Digite: [f]File Duplo, [a]Alcatra, [p]Picanha: "))
quantida_Carne = float(
    input("Informe a quantidade de carne comprada em [kg]: "))
forma_pagamento = int(input(
    "Digite a forma de pagamento: [1]Dinheiro [2]Cartão [3]pix: "))

file_duplo1 = 4.90
file_duplo2 = 5.80

Alcatra1 = 5.90
Alcatra2 = 6.80

Picanha1 = 6.90
Picanha2 = 7.80

pix = 0
dinheiro = 0


match tipo_Carne:
    case 'f':
        if(quantida_Carne <= 5):
            total = file_duplo1*quantida_Carne
        else:
            total = file_duplo2*quantida_Carne

    case 'a':
        if(quantida_Carne <= 5):
            total = Alcatra1*quantida_Carne
        else:
            total = Alcatra2*quantida_Carne

    case 'p':
        if(quantida_Carne <= 5):
            total = Picanha1*quantida_Carne
        else:
            total = Picanha2*quantida_Carne

if(forma_pagamento == 2):
    desconto = total * 0.05
    total = total-desconto
    print("Tipo de carne: ", tipo_Carne)
    print("Quantidade de carne em kg: ", quantida_Carne)
    print("Tipo de pagamento: ", forma_pagamento)
    print("Preço final: R$", total)
else:
    total
    print("Tipo de carne: ", tipo_Carne)
    print("Quantidade de carne em kg: ", quantida_Carne)
    print("Tipo de pagamento: ", forma_pagamento)
    print("Preço final: R$", total)

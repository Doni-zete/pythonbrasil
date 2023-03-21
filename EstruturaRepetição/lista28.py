quantidade_cd = int(input("Informe a quantidade de cds: "))

lista_cd = []
valor_total = 0
valor_medio = 0
for item in range(quantidade_cd):
    valor_pago = float(input(f"Informe quanto você pagou no {(item+1)}° cd: "))
    lista_cd.append(valor_pago)
    valor_total += valor_pago
    valor_medio = valor_total / quantidade_cd
print("Valor total R$ %.2f" % valor_total)
print("Média R$ %.2f" % valor_medio)

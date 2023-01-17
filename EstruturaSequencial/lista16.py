metros_quadrados = int(input("Informe o metro quadrados a ser pintado: "))


if(metros_quadrados % 54 == 0):
    calculo = metros_quadrados/54
else:
    calculo = int(metros_quadrados/54) + 1

print(calculo)

preco = calculo * 80
print('%d latas' % calculo)
print('R$ %.2f' % preco)

ganha_hora = float(input("Informe quanto você ganha por hora: "))
numero_horas = int(input("Informe o numero de horas trabalhada no mês: "))

imposto_renda = 0.11
inns = 0.08
sindicato = 0.08

salario_bruto = (ganha_hora*numero_horas)
imposto_renda = (salario_bruto*0.11)
inns = (salario_bruto*0.08)
sindicato = (salario_bruto*0.05)
salario_liquido = salario_bruto-(imposto_renda+inns+sindicato)

print("Salário Bruto : R${:.2f}".format(salario_bruto))
print("IR (11%) : R${:.2f}".format(imposto_renda))
print("INSS (8%) : R${:.2f}".format(inns))
print("Sindicato ( 5%) : R${:.2f}".format(sindicato))
print("Salário Liquido : R${:.2f}".format(salario_liquido))

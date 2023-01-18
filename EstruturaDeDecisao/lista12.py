valor_hora_trabalhada = int(input("Informe valor da hora: "))
horas_tralhada = int(input("Informe a quantidade de horas trabalhadas: "))

salario_bruto = valor_hora_trabalhada * horas_tralhada


if(salario_bruto <= 900):
    imposto_renda = 0.0

elif(salario_bruto <= 1500):
    imposto_renda = 5

elif(salario_bruto <= 2500):
    imposto_renda = 10

else:
    imposto_renda = 20

inss = salario_bruto*(10/100)
sindicato = salario_bruto*(3/100)
imposto = salario_bruto*(imposto_renda/100)
desconto = (sindicato+imposto+inss)
liquido = salario_bruto-(sindicato+imposto+inss)
fgts = salario_bruto*(11/100)


print(f"Salário Bruto R$ {salario_bruto}")
print(f"IR R$ {imposto}")
print(f"Sindicato  R$ {sindicato}")
print(f"INSS R$ {inss}")
print(f"FGTS R$ {fgts}")
print(f"Total de descontos R$ {desconto}")
print(f"Salário Liquido R$ {liquido}")

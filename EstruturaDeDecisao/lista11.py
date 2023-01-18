salario_colaborador = float(input("Informe seu salario: "))

if(salario_colaborador < 280):
    percentual = (20/100)
    aumento = salario_colaborador * percentual
    reajuste = aumento + salario_colaborador

elif(salario_colaborador >= 280 and salario_colaborador <= 700):
    percentual = (15/100)
    aumento = salario_colaborador * percentual
    reajuste = aumento + salario_colaborador

elif(salario_colaborador > 700 and salario_colaborador <= 1500):
    percentual = (10/100)
    aumento = salario_colaborador * percentual
    reajuste = aumento + salario_colaborador

elif(salario_colaborador > 1500):
    percentual = (5/100)
    aumento = salario_colaborador * percentual
    reajuste = aumento + salario_colaborador


print(f"O salário antes do reajuste R$  {salario_colaborador}")
print(f"O percentual de aumento aplicado: {percentual*100}%")
print("O valor do aumento R$ %.2f" % aumento)
print(f"O novo salário, após o aumento R$ {reajuste}")

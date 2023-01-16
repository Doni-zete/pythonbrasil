metros_quadrados = int(input("Informe o metro quadrados a ser pintado: "))


if(metros_quadrados > 3):
    calculo = metros_quadrados/3
    total = calculo/18
else:
    if(metros_quadrados < 3):
        calculo = metros_quadrados/3
        total = calculo/18

print(total)

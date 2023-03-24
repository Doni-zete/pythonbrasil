valor = int(input('Dgite um valor: '))

# Comparando se valor é menor que 1000
if(valor <= 1000):
    # Calculos
    uni = valor % 10
    dez = valor/10 % 10
    cent = valor/100 % 100
# Comparando valor
    print('Neste número a %d centenas, %d dezenas e %d unidades' %
          (cent, dez, uni))
else:
    print('Infelizmente o número %d é maior que mil' % valor)

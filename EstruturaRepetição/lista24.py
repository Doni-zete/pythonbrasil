n = int(input("Informe a quantidade de n: "))
lista_notas = []
media = 0
for item in range(n):
    nota = int(input("Informe uma nota: "))
    lista_notas.append(nota)
    media += nota/n
print(lista_notas)
print('%.2f' % media)

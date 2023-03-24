nota1, nota2 = list(map(float, (input("Informe duas notas: ").split())))

media = (nota1 + nota2)/2

if(media > 9 and media <= 10):
    print("A")
    print("APROVADO")

elif(media > 7.5 and media <= 9):
    print("B")
    print("APROVADO")

elif(media > 6 and media <= 7.5):
    print("C")
    print("APROVADO")

elif(media > 4 and media <= 6):
    print("D")
    print("REPROVADO")

elif(media > 0 and media <= 4):
    print("E")
    print("REPROVADO")

print(f"Notas: {nota1} e {nota2} media: {media}")

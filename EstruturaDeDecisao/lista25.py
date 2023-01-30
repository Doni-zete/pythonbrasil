pergunta1 = int(input("Telefonou para a vítima? [1]sim ou [0]não: "))
pergunta2 = int(input("Esteve no local do crime? [1]sim ou [0]não: "))
pergunta3 = int(input("Mora perto da vítima? [1]sim ou [0]não: "))
pergunta4 = int(input("Devia para a vítima? [1]sim ou [0]não: "))
pergunta5 = int(input("Já trabalhou com a vítima? [1]sim ou [0]não: "))


soma_respostas = pergunta1+pergunta2+pergunta3+pergunta4+pergunta5
if(soma_respostas == 5):
    print("Assassino")
elif(soma_respostas >= 3 and soma_respostas <= 4):
    print("Cúmplice")
elif(soma_respostas < 2):
    print("Inocente")
elif(soma_respostas == 2):
    print("Suspeita")

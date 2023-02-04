nome = input("Informe seu nome: ")
while(len(nome) <= 3):
    print("Nome Invalido menor que 3 caracteres\n")
    nome = input("Digite de novo seu nome: ")
print("Nome Valido maior que 3 caracteres!\n")


idade = int(input("Informe sua idade, entre 0 e 150 : "))
while(idade < 0 or idade > 150):
    print("Idade Invalida, digite entre 0 e 150\n")
    idade = int(input("Digite de novo sua idade, entre 0 e 150 : "))
print("Idade valida  dentro de 0 e 150!\n")


salario = float(input("Informe seu salario: "))
while(salario <= 0):
    print("Salario invalido\n")
    salario = float(input("Digite de novo seu salario: "))
print("Salario valido\n")

sexo = str(input("Informe seu Sexo: 'f' ou 'm': "))
while(sexo != "f" and sexo != "m"):
    print("Sexo invalido digite 'f' ou 'm':\n")
    sexo = str(input("Digite de novo seu Sexo: 'f' ou 'm': "))
print("Sexo valido!\n")


estado_civil = input("Informme seu Estado Civil: 's', 'c', 'v', 'd': ")
while(estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
    print("Estado civil Invalido!\n")
    estado_civil = input(
        "Digite de novo seu Estado Civil: 's', 'c', 'v', 'd':")
print("Estado civil valido!\n")



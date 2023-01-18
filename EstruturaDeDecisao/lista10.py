turno_estuda = str(input("Digite o turno que você estuda [m-matutino ou v-Vespertino ou n- Noturno]: "))

match turno_estuda:
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde!")
    case "n":
        print("Boa Noite!")
    case _:
        print("Valor invalido!")

arquivo_download = int(
    input("Informe o tamanho de um arquivo para download: "))
velocidade_internet = int(
    input("Informe a velocidade de um link de internet em MBps: "))

calculo = arquivo_download/(velocidade_internet/8)

print("Tempo aproximado de download: ", calculo)

import datetime
import pytz

while True:

    cidade = input("Digite a cidade: ")


    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    horario_atual_brasilia = datetime.datetime.now(fuso_brasilia)


    hora = horario_atual_brasilia.hour
    minuto = horario_atual_brasilia.minute
    segundo = horario_atual_brasilia.second


    if cidade == "Boston":
        fuso_cidade = pytz.timezone("America/New_York")
        hora = horario_atual_brasilia.astimezone(fuso_cidade).hour


    elif cidade == "Tokyo":
        fuso_cidade = pytz.timezone("Asia/Tokyo")
        hora = horario_atual_brasilia.astimezone(fuso_cidade).hour


    elif cidade == "Chicago":
        fuso_cidade = pytz.timezone("America/Chicago")
        hora = horario_atual_brasilia.astimezone(fuso_cidade).hour


    elif cidade == "Seattle":
        fuso_cidade = pytz.timezone("America/Los_Angeles")
        hora = horario_atual_brasilia.astimezone(fuso_cidade).hour


    elif cidade == "sair":
        break


    else:
        print(cidade, "não está adicionada")
        cidade = "Brasília"


    print(cidade, str(hora) + ":" + str(minuto) + ":" + str(segundo))
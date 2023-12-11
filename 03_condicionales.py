# Condicionales
dinero_que_tengo = 10

if dinero_que_tengo < 2:
    print("Comprare algo del super")
elif dinero_que_tengo < 5:
    print("Tomaré un bocata sencillo")
elif dinero_que_tengo < 12:
    print("Tomaré un menú sencillo")
else:
    ("Voy a tirar manteca al techo")

dia_semana = "martes"

match dia_semana:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case _ :
        print("Hoy no es lunes ni martes")

print("Buen provecho")
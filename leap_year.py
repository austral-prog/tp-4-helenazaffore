def leap_year():
    anio = int(input("Ingrese un año: "))
    if (anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0):
        print(f"El año {anio} es bisiestro")
    else:
        print(f"El año {anio} no es bisiestro")

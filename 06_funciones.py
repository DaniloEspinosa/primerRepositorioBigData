alumno_1 = {"nombre": "Bill", "apellido": "Gates", "ciudad": "Seattle"}
alumno_2 = {"nombre": "Steve", "apellido": "Jobs", "ciudad": "San Francisco"}
alumno_3 = {"nombre": "Jhon", "apellido": "Gonzalez", "ciudad": "San Miguel de Tucson"}
alumno_4 = {"nombre": "Goku", "apellido": "Son", "ciudad": "Paozu yama"}

alumno_2["nombre"] = "Javier"

print(alumno_2)

lista_alumnos = [
    {"nombre": "BILL", "apellido": "gATes", "ciudad": "Seattle"},
    {"nombre": "steve", "apellido": "JobS", "ciudad": "San Francisco"}
]
lista_alumnos.append(alumno_3)
lista_alumnos.append(alumno_4)

print(lista_alumnos)

def gestion_alumnos(lista):
    for alumno in lista:
        alumno["nombre"] = alumno["nombre"].capitalize()
        alumno["apellido"] = alumno["apellido"].capitalize()

print(lista_alumnos, "\n")

gestion_alumnos(lista_alumnos)

print(lista_alumnos)


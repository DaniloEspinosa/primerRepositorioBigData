# Array
producto = "donut"
mi_array = [producto, 1.5, True]
mi_array1 = ["te", 1.2, True]
print(mi_array)

# Si me gusta el café tomaré uno a 1,5€
if mi_array[2]:
    print(f"me gusta el {mi_array[0]} a {mi_array[1]}€")

if mi_array1[2]:
    print(f"me gusta el {mi_array1[0]} a {mi_array1[1]}€")

print(producto[2])

mi_array1[1] = 2.5

print(mi_array1[1])


# Diccionarios
producto_2 = {"nombre": "donut", "precio_de_venta": 1.2, "aceptacion_del_publico": False}
alumno_1 = {"nombre": "Bill", "apellido": "Gates", "ciudad": "Seattle"}
alumno_2 = {"nombre": "Steve", "apellido": "Jobs", "ciudad": "San Francisco"}
alumno_3 = {"nombre": "Jhon", "apellido": "Gonzalez", "ciudad": "San Miguel de Tucson"}

alumno_2["nombre"] = "Javier"

print(alumno_2)

# Tuplas
tupla = ("Anna", 16, "Python")
print(tupla[0])
# tupla[0] = "Sara"  --> No se puede hacer ya que las tuplas no son modificables.
tupla = list(tupla)
tupla[0] = "Sara"
tupla = tuple(tupla)
print(tupla)


# Conjuntos alias set
lista = ["Anna P", "Paco J", "Anna P", "Josep M", "Paco J"]
conjunto = set(lista)
print(conjunto)


lista_alumnos = [
    {"nombre": "Bill", "apellido": "Gates", "ciudad": "Seattle"},
    {"nombre": "Steve", "apellido": "Jobs", "ciudad": "San Francisco"}
]
lista_alumnos.append(alumno_3)

print(lista_alumnos)
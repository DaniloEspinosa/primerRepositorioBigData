producto_1 = {"nombre": "donut", "precio_de_venta": 1.2, "aceptacion_del_publico": False}
lista_nombres = ["Anna", "Pep", "eva", "Sara", "iker"]

nombre = "Danilo"
print(nombre)

for nombre in lista_nombres:
    print(f"Hola {nombre.capitalize()}!")

print(nombre)

esta_lloviendo = True

contador = 0
# while esta_lloviendo:
#     print(f"{contador} - Llevare el paraguas abierto")
#     contador += 1
#     if contador == 10:
#         esta_lloviendo = False

# print("Ya no llueve")

while esta_lloviendo:
    print("Llevare el paraguas abierto")
    llueve = input("¿Sigue lloviendo? S/N -->")
    if llueve.upper() == "N":
        esta_lloviendo = False

print("Ya no llueve")
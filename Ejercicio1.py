#Ejercicio 1: Gestion de Biblioteca (Python)
#Contexto Del Problema:
#La biblioteca "LibroFacil" necesita un programa en 
#Python para gestionar su catalogo de libros , almacenando en un archivo JSON

import json

try:
    with open('libros.json') as archivo:
        libros = json.load(archivo)
except FileNotFoundError:
    libros = []
    print("Archivo no encontrado , se creo un catalogo vacio.")


while True:
    print("\n---- MENU BIBLIOTECA ----")
    print("1.Agregar Libro")
    print("2.Prestar Libro")
    print("3.Mostrar Catalogo")
    print("4.Guardar y Salir")


    opcion = input("Seleccione una Opcion: ")


    if opcion == "1":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año = int(input("Ingre el año del libro: "))
        cantidad = int(input("Ingrese la cantidad de libro disponible: "))

        if año <= 0 or cantidad <= 0:
            print("El año o la cantida esta en negativo")
        else:
            libro = {
                "titulo" : titulo,
                "autor" : autor,
                "año" : año,
                "cantidad" : cantidad
            }

            libros.append(libro)
            print("Libro Agregado Exitosamente.")

    elif opcion == "2":
        titulo_buscar = input("Ingrese el titulo del libro a prestar: ")

        encontrado = False
        
        for libro in libros:
            if libro["titulo"].lower() == titulo_buscar.lower():
                encontrado = False
                if libro["cantidad"] > 0:
                    libro["cantidad"] -= 1
                    print("Libro prestado correctamente.")
                else:
                    print("No hay stock disponible.")
                    break
                if not encontrado:
                    print("El libro no existe en el catalogo.")

    elif opcion == "3":
        print("\n--- CATALOGO DE LIRBOS ---")
        if not libros:
            print("El catalogo esta vacio.")
        else:
            for libro in libros:
                print(f"Titulo:{libro['titulo']}")
                print(f"Autor:{libro['autor']}")
                print(f"año:{libro['año']}")
                print(f"Cantidad:{libro['cantidad']}")
                print("-" * 30)

    elif opcion == "4":
        with open("libros.json", "w") as archivo:
            json.dump(libros, archivo, indent=4)

        print("Cambios guardados correctamente. ¡Hasta luego! 👋")
        break
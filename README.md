# 📘 Proyecto de Ejercicios en Python

Este repositorio contiene una serie de **ejercicios prácticos en Python** enfocados en el uso de **archivos JSON**, **listas de diccionarios**, **manejo de errores** y **menús interactivos por consola**.

El objetivo principal es aplicar buenas prácticas de programación, validaciones de datos y persistencia de información, simulando **sistemas reales** que podrían usarse en contextos profesionales.

---

## 🧠 Tecnologías y Conceptos Utilizados

* Python 3
* Listas y diccionarios
* Archivos JSON (`json.load`, `json.dump`)
* Manejo de archivos con `with open()`
* Manejo de errores con `try-except`
* Menús interactivos con `while`
* Validación de datos de entrada

---

# 📚 Ejercicio 1: Gestión de Biblioteca

## Contexto

La biblioteca **“LibroFácil”** necesita un programa en Python para gestionar su catálogo de libros, almacenado de forma persistente en un archivo `libros.json`.

## Requerimientos Funcionales

1️⃣ **Cargar Catálogo**

* Al iniciar el programa, se deben cargar los datos desde `libros.json`.
* Si el archivo no existe, se debe crear una lista vacía e informar al usuario.

2️⃣ **Agregar Libro**

* Solicitar al usuario:

  * Título (string)
  * Autor (string)
  * Año (entero)
  * Cantidad disponible (entero)
* Validar que el año y la cantidad no sean negativos.

3️⃣ **Prestar Libro**

* Buscar un libro por su título.
* Si hay stock disponible, reducir la cantidad en 1.

4️⃣ **Mostrar Catálogo**

* Listar todos los libros registrados.
* Mostrar un mensaje si el catálogo está vacío.

5️⃣ **Guardar y Salir**

* Guardar los cambios realizados en `libros.json`.

## Requerimientos Técnicos

* Lista de diccionarios
* Uso de `json.load()` y `json.dump()`
* Manejo de archivos con `with open()`
* Manejo de errores con `try-except` y `FileNotFoundError`
* Menú interactivo con ciclo `while`

---



# 📚 Guía rápida para el examen – Gestión de Biblioteca en Python

Bro, esto es tu **chuleta legal** 😎. Léelo antes del examen y vas fino.

---

## 🧠 Idea clave del ejercicio

El programa **gestiona un catálogo de libros** usando un archivo `libros.json`.

👉 Todo gira alrededor de:

* Listas
* Diccionarios
* Archivos JSON
* `try / except`
* Menú con `while True`

---

## 📂 Estructura básica del archivo

```python
import json
```

Siempre va primero. Sin esto, JSON no existe 😅.

---

## 1️⃣ Cargar el catálogo (MUY importante)

💡 Esto **SIEMPRE cae en el examen**.

```python
try:
    with open('libros.json') as archivo:
        libros = json.load(archivo)
except FileNotFoundError:
    libros = []
    print("Archivo no encontrado, se creó un catálogo vacío")
```

🔑 Qué recordar:

* `try` → intenta abrir el archivo
* `except FileNotFoundError` → si no existe
* `libros = []` → empezamos vacío

📌 Frase mental para el examen:

> *Si no hay archivo, no hay drama, creo la lista vacía.*

---

## 2️⃣ Estructura de un libro (diccionario)

Cada libro es así:

```python
libro = {
    "titulo": titulo,
    "autor": autor,
    "anio": anio,
    "cantidad": cantidad
}
```

Y se guarda con:

```python
libros.append(libro)
```

🧠 Truco:

* **Lista de diccionarios** = catálogo completo

---

## 3️⃣ Validaciones básicas

Nunca guardes datos raros 👀:

```python
if anio < 0 or cantidad < 0:
    print("Datos inválidos")
else:
    libros.append(libro)
```

📌 OJO en el examen:

* `or` → cuando **uno solo** sea incorrecto
* `and` → cuando **ambos** deban cumplirse

---

## 4️⃣ Mostrar el catálogo (opción 3 del menú)

Forma básica (válida en examen):

```python
print(libros)
```

Forma pro (te da puntos extra 😏):

```python
print("\n--- CATÁLOGO ---")
for libro in libros:
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Año: {libro['anio']}")
    print(f"Cantidad: {libro['cantidad']}")
    print("-" * 20)
```

---

## 5️⃣ Guardar cambios en el archivo (opción 4)

🔥 ESTA ES CLAVE 🔥

```python
with open('libros.json', 'w') as archivo:
    json.dump(libros, archivo, indent=4)
print("Cambios guardados correctamente")
```

🧠 Memoriza:

* `'w'` → escribir
* `json.dump()` → guardar
* `indent=4` → bonito (profe feliz)

---

## 6️⃣ Menú principal (estructura típica)

```python
while True:
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Mostrar catálogo")
    print("4. Guardar y salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
```

📌 En el examen:

* El menú **SIEMPRE va en `while True`**
* Salir = `break`

---

## 🧠 Chuleta mental express (último minuto)

✔ JSON → `json.load()` / `json.dump()`
✔ Archivo no existe → `try / except FileNotFoundError`
✔ Catálogo → lista `[]`
✔ Libro → diccionario `{}`
✔ Menú → `while True`
✔ Guardar → `'w'`

---

## 😎 Consejo final de pana

Si te bloqueas en el examen:

1. Escribe primero el `try / except`
2. Luego el `while True`
3. Después completas las opciones

Eso ya te asegura **la mitad de los puntos** mínimo.

---

🔥 Si quieres, en el próximo mensaje te hago:

* Un **ejercicio tipo examen**
* O una **chuleta aún más corta** (1 página)

Tú mandas, crack 💪



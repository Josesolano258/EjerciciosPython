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

# 🎓 Ejercicio 2: Sistema de Alumnos

## Contexto

Una academia necesita registrar alumnos y sus notas finales utilizando un archivo `alumnos.json`.

## Requerimientos Funcionales

1️⃣ **Cargar Datos**

* Leer los datos desde `alumnos.json` al iniciar el programa.

2️⃣ **Agregar Alumno**

* Solicitar:

  * Nombre (string)
  * Edad (entero ≥ 0)
  * Nota final (float entre 0 y 10)

3️⃣ **Modificar Nota**

* Buscar al alumno por nombre.
* Permitir actualizar su nota final.

4️⃣ **Mostrar Alumnos**

* Listar todos los alumnos registrados.

5️⃣ **Guardar y Salir**

* Guardar los cambios en `alumnos.json`.

## Requerimientos Técnicos

* Lista de diccionarios
* Validación de rangos numéricos
* Manejo de excepciones con `try-except`
* Uso exclusivo de la librería `json`

---

# 🧑‍💼 Ejercicio 3: Control de Empleados

## Contexto

La empresa **“SoftJobs”** desea administrar la información de sus empleados desde la consola, utilizando persistencia en un archivo `empleados.json`.

## Requerimientos Funcionales

1️⃣ **Cargar Empleados**

* Leer datos desde `empleados.json`.

2️⃣ **Agregar Empleado**

* Solicitar:

  * Nombre (string)
  * Puesto (string)
  * Salario (float ≥ 0)

3️⃣ **Actualizar Salario**

* Buscar empleado por nombre.
* Permitir modificar su salario.

4️⃣ **Mostrar Empleados**

* Listar todos los empleados registrados.

5️⃣ **Guardar y Salir**

* Guardar los cambios realizados.

## Requerimientos Técnicos

* Lista de diccionarios
* Manejo de errores de conversión (`ValueError`)
* Manejo de `FileNotFoundError`
* Menú interactivo con `while True`

---

# 🧾 Ejercicio 4: Registro de Ventas

## Contexto

Una tienda necesita registrar sus ventas diarias y almacenarlas en un archivo `ventas.json`.

## Requerimientos Funcionales

1️⃣ **Cargar Ventas**

* Leer datos desde `ventas.json`.

2️⃣ **Registrar Venta**

* Solicitar:

  * Producto (string)
  * Precio (float > 0)
  * Cantidad (int > 0)

3️⃣ **Mostrar Ventas**

* Listar todas las ventas con el total calculado por producto.

4️⃣ **Total General**

* Mostrar el total general vendido.

5️⃣ **Guardar y Salir**

* Guardar los cambios en `ventas.json`.

## Requerimientos Técnicos

* Lista de diccionarios
* Cálculos aritméticos básicos
* Manejo de errores con `try-except`
* Persistencia con `json.dump()`

---

# 📇 Ejercicio 5: Agenda de Contactos

## Contexto

Se requiere una agenda digital en Python que permita almacenar contactos de forma persistente en `contactos.json`.

## Requerimientos Funcionales

1️⃣ **Cargar Contactos**

* Leer contactos desde `contactos.json`.

2️⃣ **Agregar Contacto**

* Solicitar:

  * Nombre (string)
  * Teléfono (string)
  * Email (string)

3️⃣ **Editar Contacto**

* Buscar contacto por nombre.
* Permitir editar el número de teléfono.

4️⃣ **Mostrar Contactos**

* Listar todos los contactos registrados.

5️⃣ **Guardar y Salir**

* Guardar los cambios realizados.

## Requerimientos Técnicos

* Lista de diccionarios
* Manejo de archivos con `with open()`
* Manejo de excepciones
* Menú interactivo por consola

---

## ✅ Buenas Prácticas Aplicadas

* Separación clara de responsabilidades
* Validación de datos ingresados por el usuario
* Manejo adecuado de errores
* Uso correcto de archivos JSON
* Código legible, mantenible y escalable

---

🚀 **Este proyecto representa un conjunto de ejercicios completamente funcionales, tolerantes a errores y alineados con prácticas reales de desarrollo en Python.**

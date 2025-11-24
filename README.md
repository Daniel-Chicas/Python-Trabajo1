# 📘 Calculadora de Promedios – Proyecto en Python

Este proyecto consiste en una aplicación en Python que permite registrar materias y sus calificaciones, calcular estadísticas relevantes y mostrar un resumen final completamente procesado. Está desarrollado **exclusivamente con programación estructurada**, sin clases ni POO.

---

## 📌 Requisitos del Programa

- ✏️ Permitir al usuario ingresar nombres de materias y sus calificaciones (entre 0 y 10).
- 📂 Almacenar materias y calificaciones en **listas**.
- 🧮 Calcular el **promedio general** de todas las calificaciones.
- ✔️ Determinar materias **aprobadas** y **reprobadas** según un umbral (5.0).
- ⬆️⬇️ Identificar la calificación **más alta** y **más baja**.
- ➕ Permitir ingresar tantas materias como el usuario desee.
- 📑 Mostrar un **resumen final** con toda la información procesada.
- 🔧 Utilizar **al menos 3 funciones** para organizar el código.
- 🛡️ Incluir **validación básica** de entradas.
- 🚫 No usar programación orientada a objetos (sin clases).

---

## 📝 Instrucciones de Implementación

### 1️⃣ Archivo principal

Crea un archivo llamado **`calculadora_promedios.py`** donde se desarrollará todo el programa.

---

### 2️⃣ Función `ingresar_calificaciones()`

Esta función debe:

- Solicitar el nombre de cada materia.
- Pedir una calificación válida (0–10), validando que sea un número dentro del rango.
- Guardar los valores en **dos listas separadas**:
  - `materias`
  - `calificaciones`
- Preguntar si el usuario desea continuar registrando datos.
- Retornar ambas listas cuando el usuario decida terminar.

---

### 3️⃣ Función `calcular_promedio(calificaciones)`

Esta función debe:

- Recibir una lista de calificaciones.
- Devolver el **promedio general** de todas ellas.

---

### 4️⃣ Función `determinar_estado(calificaciones, umbral)`

Debe:

- Recibir la lista de calificaciones y un valor umbral (por defecto `5.0`).
- Devolver dos listas:
  - Índices de materias **aprobadas**.
  - Índices de materias **reprobadas**.

---

### 5️⃣ Función `encontrar_extremos(calificaciones)`

Debe:

- Identificar el índice de la calificación **más alta**.
- Identificar el índice de la calificación **más baja**.
- Retornar ambos índices.

---

### 6️⃣ Función principal `main()`

La función principal debe:

1. Llamar a `ingresar_calificaciones()` para obtener las listas de materias y calificaciones.
2. Usar `calcular_promedio()` para obtener el promedio general.
3. Usar `determinar_estado()` para saber qué materias están aprobadas y reprobadas.
4. Usar `encontrar_extremos()` para identificar la mejor y la peor calificación.
5. Mostrar un **resumen final** que incluya:
   - Todas las materias con sus calificaciones.
   - El promedio general.
   - Las materias aprobadas y reprobadas.
   - La materia con mejor calificación y su valor.
   - La materia con peor calificación y su valor.
6. Manejar casos especiales, como cuando no se ingresa ninguna materia.
7. Finalizar el programa con un **mensaje de despedida**.
8. Incluir la estructura:

```python
if __name__ == "__main__":
    main()
```

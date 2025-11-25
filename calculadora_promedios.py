import os
import sys

listaCursos = []
listaNotas = []
umbralAprobados = 5

def main():
    while True:
        limpiar_pantalla()
        opcion = ""
        print("""
                     CALCULADORA DE PROMEDIOS
            ===========================================
            1. Ingresar materias y calificaciones
            2. Calcular promedio general
            3. Mostrar materias aprobadas y reprobadas
            4. Mostrar materia con mejor y peor calificación
            5. Mostrar resumen completo
            6. Salir del programa""")
        opcion = input(">>> Seleccione una opción: ")
        if opcion == "1":
            limpiar_pantalla()
            print("Ingresar materias y calificaciones")
            ingresar_calificaciones()
        elif opcion == "2":
            limpiar_pantalla()
            print("Calcular promedio general")
            mostrarPromedioGeneral()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            limpiar_pantalla()
            print("Mostrar materias aprobadas y reprobadas")
            mostrarMateriasAprobadasYReprobadas()
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            limpiar_pantalla()
            print("Mostrar materia con mejor y peor calificación")
            mostrarMejorPeorCalificacion()
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            limpiar_pantalla()
            print("RESUMEN DE CURSOS Y CALIFICACIONES INGRESADAS")
            print("===============================================")
            print(">>>>> LISTADO DE MATERIAS Y CALIFICACIONES <<<<<")
            mostrarListadoCursos()
            print("================================================")
            print(">>>>> PROMEDIO GENERAL <<<<<")
            mostrarPromedioGeneral()
            print("================================================")
            print(">>>>> MATERIAS APROBADAS Y REPROBADAS <<<<<")
            mostrarMateriasAprobadasYReprobadas()
            print("================================================")
            print(">>>>> MEJOR Y PEOR CALIFICACIÓN <<<<<")
            mostrarMejorPeorCalificacion()
            print("================================================")
            input("\nPresione Enter para continuar...")
        elif opcion == "6":
            limpiar_pantalla()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

    print("Saliendo del programa. ¡Hasta luego!")

def ingresar_calificaciones():
    while True:
        curso = input("Ingrese el nombre de la materia (o 'salir' para terminar): ")
        if curso.lower() == 'salir':
            break
        try:
            if curso in listaCursos:
                print("La materia ya ha sido ingresada. Intente con otra.")
                continue
            while True:
                nota = float(input(f"Ingrese la calificación para {curso}: "))
                if 0 <= nota <= 10:
                    listaCursos.append(curso)
                    listaNotas.append(nota)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingrese un número válido para la calificación.")
    print(">>>>> Calificaciones ingresadas correctamente. <<<<<")
    mostrarListadoCursos()
    input("\nPresione Enter para continuar...")

def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral):
    indices_aprobadas = []
    indices_reprobadas = []

    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            indices_aprobadas.append(i)
        else:
            indices_reprobadas.append(i)

    return indices_aprobadas, indices_reprobadas

def encontrar_extremos(calificaciones):
    """
    Debe devolver los índices de las calificaciones extrema:
    - índice de la calificación más alta
    - índice de la calificación más baja
    """
    if len(calificaciones) == 0:
        return None, None

    max_nota = max(calificaciones)
    min_nota = min(calificaciones)
    indice_max = calificaciones.index(max_nota)
    indice_min = calificaciones.index(min_nota)

    return indice_max, indice_min

def limpiar_pantalla():
    if sys.platform == 'win32':
        os.system('cls')

def mostrarPromedioGeneral():
    promedio = calcular_promedio(listaNotas)
    if len(listaNotas) == 0:
        print("No hay calificaciones para calcular el promedio.")
    else:
        print(f"El promedio general es: {promedio:.2f}")

def mostrarListadoCursos():
    if len(listaCursos) == 0:
        print("No hay materias registradas.")
    else:
        print("Listado de materias y calificaciones:")
        for i in range(len(listaCursos)):
            print(f"{listaCursos[i]}: {listaNotas[i]}")

def mostrarMateriasAprobadasYReprobadas():
    indices_aprobadas, indices_reprobadas = determinar_estado(listaNotas, umbralAprobados)

    print("Materias Aprobadas:")
    if not indices_aprobadas:
        print("- Ninguna")
    else:
        for i in indices_aprobadas:
            print(f"- {listaCursos[i]} ({listaNotas[i]})")

    print("\nMaterias Reprobadas:")
    if not indices_reprobadas:
        print("- Ninguna")
    else:
        for i in indices_reprobadas:
            print(f"- {listaCursos[i]} ({listaNotas[i]})")

def mostrarMejorPeorCalificacion():
    indice_max, indice_min = encontrar_extremos(listaNotas)
    if indice_max is not None and indice_min is not None:
        print(f"Mejor calificación: {listaCursos[indice_max]} con {listaNotas[indice_max]}")
        print(f"Peor calificación: {listaCursos[indice_min]} con {listaNotas[indice_min]}")
    else:
        print("No hay calificaciones ingresadas.")

if __name__ == "__main__":
    main()

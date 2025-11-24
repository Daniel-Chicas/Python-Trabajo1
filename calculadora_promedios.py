import os
import sys

listaCursos = []
listaNotas = []
umbralAprobados = 5

def main():
    while(True):
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
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
        
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
    aprobadas, reprobadas = [], []
    indiceAprobada, indiceReprobada = [], []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append((listaCursos[i]))
            indiceAprobada.append(i)
        else:
            reprobadas.append((listaCursos[i]))
            indiceReprobada.append(i)
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    if len(calificaciones) == 0:
        return None, None
    max_nota = max(calificaciones)
    min_nota = min(calificaciones)
    indice_max = calificaciones.index(max_nota)
    indice_min = calificaciones.index(min_nota)
    return (listaCursos[indice_max], max_nota), (listaCursos[indice_min], min_nota)

def limpiar_pantalla():
    if sys.platform == 'win32':
        os.system('cls')

def mostrarPromedioGeneral():
    promedio = calcular_promedio(listaNotas)
    print(f"El promedio general es: {promedio:.2f}")

def mostrarListadoCursos():
    print("Listado de materias y calificaciones:")
    for i in range(len(listaCursos)):
        print(f"{listaCursos[i]}: {listaNotas[i]}") 

def mostrarMateriasAprobadasYReprobadas():
    aprobadas, reprobadas = determinar_estado(listaNotas, umbralAprobados)
    print("Materias Aprobadas:")
    for materia in aprobadas:
        print(f"- {materia}")
    print("\nMaterias Reprobadas:")
    for materia in reprobadas:
        print(f"- {materia}")

def mostrarMejorPeorCalificacion():
    mejor, peor = encontrar_extremos(listaNotas)
    if mejor and peor:
        print(f"Mejor calificación: {mejor[0]} con {mejor[1]}")
        print(f"Peor calificación: {peor[0]} con {peor[1]}")
    else:
        print("No hay calificaciones ingresadas.")

if __name__ == "__main__":
    main()
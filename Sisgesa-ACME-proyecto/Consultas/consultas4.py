import json
from pathlib import Path


def consultar_estud_en_grupo():
    archivo_asignacion = Path("asignacion.json")
    if not archivo_asignacion.is_file():
        print("No se encontró el archivo de asignación.")
        return 
    try:
        with open(archivo_asignacion, "r") as fd:
            asignacion = json.load(fd)
    except Exception as e :
        print("Error al abrir el archivo de asignación:", e)
        return
    
    est_consultar=input("codigo del estudiante a consultar? ")

    for grupo, datos in asignacion.items():
        if est_consultar in datos["estudiantes"]:
            print(f"el estudante {est_consultar} esta matriculado en el grupo {grupo} .")
            return
        
    print(f"el estudiante {est_consultar} no esta matriculado en ningun grupo. ")



def consultar_estud_modulo():
    archivo_asignacion = Path("asignacion.json")
    if not archivo_asignacion.is_file():
        print("No se encontró el archivo de asignación.")
        return 
    try:
        with open(archivo_asignacion, "r") as fd:
            asignacion = json.load(fd)
    except Exception as e :
        print("Error al abrir el archivo de asignación:", e)
        return
    
    cod_modulo=input("codigo del modulo a consultar? ")
    encuentra_estudiante_en_modulo = []


    for grupo, datos in asignacion.items():
        if cod_modulo in datos["modulos"]:
            encuentra_estudiante_en_modulo.extend(datos["estudiantes"])
    if encuentra_estudiante_en_modulo:
            print(f"los estudiantes matriculados en el modulo {cod_modulo}: {', '.join(encuentra_estudiante_en_modulo)}.")
    else:
        print(f"no hay estudiantes matriculados en el modulo {cod_modulo}.")




def docente_por_modulo():
  
    try:
        with open("Registro_de_docentes.json", "r") as f:
            docentes = json.load(f)        
    except Exception as e:
        print(f"Error al cargar Registro_de_docentes.json: {e}")
        return

    try:
        with open("registro de modulos.json", "r") as f:
            modulos = json.load(f)        
    except Exception as e:
        print(f"Error al cargar registro de modulos.json: {e}")
        return

    # Consultar y mostrar docentes que imparten módulos
    for cedula, docente in docentes.items():
        # Corregir la clave eliminando el espacio extra en "modulos "
        modulos_docente = docente.get("modulos", [])

        # Imprimir los módulos que el docente dicta
        print(f"Módulos dictados por {docente['nombre del docente']}: {modulos_docente}")

        # Obtener nombres de módulos a partir de los códigos (si fuera necesario)
        modulos_dictados = [modulos[modulo]["nombre de modulo"] for modulo in modulos_docente if modulo in modulos]

        # Imprimir los resultados si hay módulos dictados
        if modulos_dictados:
            print(f"{docente['nombre del docente']} (Cédula: {cedula}) dicta {', '.join(modulos_dictados)}\n")



def estudiantes_a_cargo_docente():
    print(" en proseso .... :(")



def sub_menu ():
    while True:
        print(" 1- Consultar los estudiantes matriculados en un grupo. ")
        print(" 2- Consultar los estudiantes inscritos en un módulo. ")
        print(" 3- Consultar los docentes que imparten un módulo. ")
        print(" 4- Consultar los estudiantes a cargo de un docente en un módulo. ")
        print(" 5- <---- volver al menu principal.")

        try:
            op = int(input("---> Opción: ")) 
            if op < 1 or op > 5:
                print("Error: opción no válida")
                print("Presione cualquier tecla para volver al menú.")
                continue           
            match op:
                case 1:
                    consultar_estud_en_grupo()
                case 2:
                    consultar_estud_modulo()
                case 3:
                    docente_por_modulo()
                case 4:
                    print("-En Proceso... ---")
                case 5: 
                    print("Saliendo del menu...")
                    break
        except ValueError:
            print("Error.  opcion no valida")
            print("presione cualquier tecla para volver al menu")
            

       
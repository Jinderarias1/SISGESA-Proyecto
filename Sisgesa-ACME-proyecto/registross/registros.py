import json
from pathlib import Path

def Registro_de_grupos():
    archivo = Path("registro_grupos.json")
    grupos = {}
    if archivo.is_file():
        try:
            with open("registro_grupos.json", "r") as fd:
                grupos = json.load(fd)
            if not fd.closed: 
                fd.close()
        except Exception as e :
            print(" error al abrir al archivo.  " + e)
    else:
        print("error. el archivo no exixte se creara uno nuevo .")
        input(" presione cualquier tecla para continuar... ")
    while True:
        id_grupo = input("ingrese el id del grupo: ")

        if id_grupo not in grupos:
            nom_grupo = input("Ingrese el nombre del grupo: ")
            siglas_grupo = input("Siglas del grupo: ")

            grupos[id_grupo] = {
                "nombre del grupo" : nom_grupo,
                "siglas del grupo" : siglas_grupo, 
                
            }
            grupos =dict(sorted(grupos.items()))

            with open("registro_grupos.json", "w") as archivo:
                json.dump(grupos, archivo)
            print("grupo guardado en registro_grupos.json")
        else:
            print("ese codigo ya esta asociado con otro grupo.")

        continuar = input("¿Desea agregar otro grupo? (S/N): ").upper()
        if continuar != 'S':
            break

    input("Presione cualquier tecla para volver al menu.")
    return id_grupo

def Registro_de_módulos():
    archivo = Path("registro de modulos.json")
    modulos = {}
    if archivo.is_file():
        try:
            with open("registro de modulos.json", "r") as fd:
                modulos = json.load(fd)
            if not fd.closed: 
                fd.close()
        except Exception as e :
            print(" error al abrir al archivo.  " + e)
    else:
        print("error. el archivo no exixte se creara uno nuevo.")
        input(" presione cualquier tecla para continuar... ")

    while True:
        id_modulo = input("ingrese el id del modulo: ")
        if id_modulo not in modulos:
            nom_modulo = input("ingrese el nombre del modulo: ")
            duracion_sem = int(input("Ingrese la duracion en semanas del modulo: "))

            modulos[id_modulo] = {
                "nombre de modulo" : nom_modulo,
                "duracion en semanas del modulo" : duracion_sem
            }

            modulos = dict(sorted(modulos.items()))

            with open("registro de modulos.json", "w") as archivo:
                json.dump(modulos, archivo)
            print("modulo guardado en registro de modulos.json ")
        else:
            print("el codigo ya esta asociado para otro modulo. ")
        
        continuar = input("¿Desea agregar otro modulo? (S/N): ").upper()
        if continuar != 'S':
            break
    input("Presione cualquier tecla para volver al menú.")
    return id_modulo

def Registro_de_estudiantes():
    
    archivo = Path("Registro de estudiantes.json")
    registro = {}
    if archivo.is_file():
        try:
            with open("Registro de estudiantes.json", "r") as fd:
                registro = json.load(fd)
            if not fd.closed:
                fd.close()
        except Exception as e :
            print(" error al abrir al archivo.  " + e)
    else:
        print("error. el archivo no exixte se creara uno nuevo.")
        input(" presione cualquier tecla para continuar... ")
    
    while True:

        id_estudiante = input("Estudiante, ingrese su ID: ")

        if id_estudiante not in registro:
            nom_estudiante = input("Ingrese su nombre: ")

        # Validar el sexo ingresado
            while True:
                sexo = input("Ingrese su sexo (M/F): ").upper()  # Convertir a mayúsculas
                if sexo in ["M", "F"]:
                    break  # Sale del ciclo si es válido
                print("Sexo no válido. Debe ingresar 'M' para masculino o 'F' para femenino.")

            edad = int(input("Ingrese su edad: "))
        
            # Añadir el nuevo estudiante al registro
            registro[id_estudiante] = {
            "nombre del estudiante": nom_estudiante,
            "sexo": sexo,
            "edad": edad
        }

            # Guardar todos los registros en el archivo JSON
            with open("Registro de estudiantes.json", "w") as archivo:
                json.dump(registro, archivo)  # Usar indentación para legibilidad
                print("Datos guardados en '{}'.".format("Registro de estudiantes.json"))
        else:
            print("El ID ingresado ya está asociado a otro estudiante.")
        continuar = input("¿Desea agregar otro estudiante? (S/N): ").upper()
        if continuar != 'S':
            break
    input("Presione cualquier tecla para volver al menú.")
    return id_estudiante

def Registro_de_docentes():

# abrir json 
    archivo = Path("Registro_de_docentes.json")
    reg_docentes = {}
    if archivo.is_file():
        try:
            with open("Registro_de_docentes.json", "r") as fd:
                reg_docentes = json.load(fd)
            if not fd.closed: 
                fd.close()
        except Exception as e :
            print(" error al abrir al archivo.  " + e)
    else:
        print("error. el archivo no exixte se creara uno nuevo.")
        input(" presione cualquier tecla para continuar... ")

# registro de docente
    while True:

        ced_docentes = int(input("Ingrese cedula: "))
        if ced_docentes not in reg_docentes:
            nom_docente = input("ingrese su nombre: ")


        modulos_dictados = int(input("cuantos modulos dicta: "))
        
        modulos = []
        if modulos_dictados <= 3:
            for i in range (modulos_dictados):
                nom_del_modulos = input(f"ingrese nombre del modulo { i + 1}: ")
                modulos.append(nom_del_modulos)
        

            reg_docentes [ced_docentes] = {
            "nombre del codente" : nom_docente,
            "modulos " : modulos
        }
# guardar en json  
        

            with open("Registro_de_docentes.json", "w") as archivo:
                json.dump(reg_docentes, archivo)
                print("modulo guardado en Registro_de_docentes.json ")
        else:
            print("La cedula ya esta registrada a otro docente.")
        continuar = input("¿Desea agregar otro docente? (S/N): ").upper()
        if continuar != 'S':
            break

    input("presione cualquier tecla para volver al menu. ")
    return reg_docentes 

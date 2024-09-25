import json
from pathlib import Path

def asignar_grupos_modulos_docentes():
    # Abrir el archivo JSON de asignaciones; si no existe, se creará uno nuevo.
    archivo_asignacion = Path("asignacion.json")
    asignacion = {}  

    # Si ya hay un archivo JSON, cargar las asignaciones existentes.
    if archivo_asignacion.is_file():
        try:
            with open(archivo_asignacion, "r") as fd:
                asignacion = json.load(fd)  
        except Exception as e:
            print("Error al abrir el archivo de asignación:", e)

    # Cargar estudiantes desde otro archivo JSON.
    registro = {}
    archivo_estudiantes = Path("Registro de estudiantes.json")
    if archivo_estudiantes.is_file():#verificar si existe
        with open(archivo_estudiantes, "r") as fd:
            registro = json.load(fd)

    # Cargar grupos desde otro archivo JSON.
    grupos = {}
    archivo_grupos = Path("registro_grupos.json")
    if archivo_grupos.is_file():
        with open(archivo_grupos, "r") as fd:
            grupos = json.load(fd)  # Cargar la información de los grupos.

    # Cargar módulos desde otro archivo JSON.
    modulos = {}
    archivo_modulos = Path("registro de modulos.json")
    if archivo_modulos.is_file():
        with open(archivo_modulos, "r") as fd:
            modulos = json.load(fd)  # Cargar la información de los módulos.

    # Bucle para asignar estudiantes a grupos y módulos.
    while True:
        # Solicitar el código del estudiante.
        print("vamos a asignar un estudiante a un modulo y a un grupo.")
        int_cog = input("Introduzca el código del estudiante: ")

        # Verificar si el estudiante existe en el registro.
        if int_cog not in registro:
            print("Este estudiante no existe.")
            continue

        # Preguntar por el código del módulo.
        codigo_modulo = input("Introduzca el código del módulo: ")
        if codigo_modulo not in modulos:
            print("El código del módulo no existe.")
            continue
        
        # Mostrar grupos disponibles para la asignación.
        print("Grupos disponibles:")
        for grupo in grupos.keys():
            print(grupo)

        # Preguntar a qué grupo desea asignar el módulo.
        asig = input("¿A qué grupo desea asignar el módulo?: ")

        # Verificar si el grupo existe.
        if asig not in grupos:
            print("El código del grupo no existe. Intente nuevamente.")
            continue

        # Verificar si el estudiante ya está asignado a otro grupo.
        for grupo, datos in asignacion.items():
            if int_cog in datos.get("estudiantes", []):
                cambiar = input(f"El estudiante {int_cog} ya está registrado en '{grupo}'. ¿Desea cambiarlo? (S/N): ")
                if cambiar.upper() == 'S':
                    datos["estudiantes"].remove(int_cog)  # Remover al estudiante del grupo anterior.
                    print(f"El estudiante {int_cog} ha sido eliminado del grupo '{grupo}'.")

        # Asignar el estudiante y el módulo al grupo.
        if asig not in asignacion:
            asignacion[asig] = {
                "estudiantes": [],  # Crear lista para estudiantes.
                "modulos": []       # Crear lista para módulos.
            }
        asignacion[asig]["estudiantes"].append(int_cog)  # Agregar el estudiante a la lista.
        asignacion[asig]["modulos"].append(codigo_modulo)  # Agregar el módulo a la lista.

        # Guardar las asignaciones en el archivo JSON.
        try:
            with open(archivo_asignacion, "w") as archivo_estudiantes:
                json.dump(asignacion, archivo_estudiantes)  # Guardar las asignaciones sin indentación.
            print(f"Estudiante {int_cog} guardado en el grupo '{asig}' con el módulo '{codigo_modulo}'.")
        except Exception as e:
            print("Error al guardar las asignaciones:", e)

        # Preguntar si se quiere agregar otro estudiante.
        if input("¿Quieres agregar otro estudiante a un grupo? (S/N): ").upper() != 'S':
            break

        print("Asignaciones guardadas correctamente.")



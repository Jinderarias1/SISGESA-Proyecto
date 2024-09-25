def Menu1():
    while True:
        print("                                1- Registro de grupos.                                ") 
        print("                                2- Registro de módulos.                                ")
        print("                                3- Registro de estudiantes.                               ") 
        print("                                4- Registro de docentes.                                 ")
        print("                                5- Asignar grupos modulos estudiantes.                                ") 
        print("                                6- Consultas de información.                                ") 
        print("                                7- Generación de informes.                                ")
        print("                                8- Cambio de contraseña.                                   ") 
        print("                                9- Salida del sistema.                                    ") 
    
        print("---> opcion ?",end="")
        try:
            Opcion = int(input())
            if Opcion < 1 or Opcion >9:
                print("error opcion no valida")
                print("presione cualquier tecla para volver al menu")
                continue
            return Opcion
        except ValueError:
            print("error opcion no valida")
            print("presione cualquier tecla para volver al menu")

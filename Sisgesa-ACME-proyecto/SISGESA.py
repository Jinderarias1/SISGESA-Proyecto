
from Consultas.consultas4 import *
from Menus.Requerimientos_ import *
from contra_cambio_salida.cambio_contra import  *
from registross.registros import *
from contra_cambio_salida.inicio__ import *
from asignar_grupos_modulos_estud.asignacion_de_grupos_y_modulos import *


print("                        Bienvenido al Sotfware SISGESA de la empresa ACME                                   ")
print("  ")
iniciarce()

while True: 
    op = Menu1()
    match op:
        case 1:
            Registro_de_grupos()    
        case 2:
            Registro_de_módulos()
        case 3:
            Registro_de_estudiantes()
        case 4:
            Registro_de_docentes()
        case 5:
            asignar_grupos_modulos_docentes()
        case 6:
         sub_menu()
        case 7:
            print("En proceso...   ")
        case 8:
            cambiar_contraseña()          
        case 9:
            print("GRACIAS por usar el software.\n")
            break 


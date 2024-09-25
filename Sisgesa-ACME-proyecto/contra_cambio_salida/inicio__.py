import hashlib
import json




def encriptar(contraseña):
    return hashlib.sha256(contraseña.encode("utf-8")).hexdigest() 
contraseña = "SISGESA"
contraseña_encriptada = encriptar(contraseña)
guardar_contraseña = {"contra encriptada" :contraseña_encriptada}
with open("contraseña.json", "w") as archivo:
    json.dump(guardar_contraseña, archivo)
    print(" ")

def iniciarce ():
    contraseña = hashlib.sha256("SISGESA".encode("utf-8")).hexdigest()
    nom_usua = input("nombre de usuario: ")
    
    while True:
        ingr_contra= input("ingrese la contraseña: ")
        ingr_contra_hash = hashlib.sha256(ingr_contra.encode("utf-8")).hexdigest()

        if ingr_contra_hash != contraseña:
            print("la contraseña es incorrecta.")  
        else:
            print(" ")
            print("                               la contraseña es correcta                                ")
            print(f"                                 BIENVENIDO {nom_usua}                                 ")
            print(" ")
            break

     
           
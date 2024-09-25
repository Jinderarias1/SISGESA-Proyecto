import hashlib 
import json

def cambiar_contraseña():
    # Cargar la contraseña encriptada existente desde el archivo
    with open("contraseña.json", "r") as archivo:
        guardar_contraseña = json.load(archivo)

    contraseña_encriptada_actual = guardar_contraseña["contra encriptada"]
    print("CAMBIO DE CONTRASEÑA.")
    
    usua_contra = input("Ingrese contraseña nueva: ")
    nueva_contra = hashlib.sha256(usua_contra.encode("utf-8")).hexdigest()
    
    # Reemplazar la contraseña encriptada en el diccionario
    guardar_contraseña["contra encriptada"] = nueva_contra

    # Guardar la nueva contraseña encriptada en el archivo
    with open("contraseña.json", "w") as archivo:
        json.dump(guardar_contraseña, archivo)

    print("Contraseña cambiada y guardada en contraseña.json")


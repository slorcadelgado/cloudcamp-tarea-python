import os
import shutil
from datetime import datetime

def create_folder():
    
    try:
        #Se crea la carpeta con un nombre dinámico basado en la fecha (formato de la fecha DD-MM-YYYY)
        folder = datetime.now().strftime("folder_%d-%m-%Y")
        
        #Si ya existe una carpeta con el mismo nombre se elimina
        if os.path.exists(folder):
            #Se elimina las carpeta y todos los archivos dentro de ella
            shutil.rmtree(folder)
            print(f"Folder '{folder}' deleted.")

        #Se crea la carpeta
        os.makedirs(folder)
        print(f"Folder '{folder}' created.")

        #Crear 10 archivos dentro de la carpeta y su contenido tiene la fecha y hora de creación (formato DD/MM/YYYY HH:MM:SS)
        for i in range(1, 11):
            file_name = f"file_{i}.txt"
            route = os.path.join(folder, file_name)
            with open(route, "w") as file:
                date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                file.write(f"Date and Time: {date_time}")
                file.close()
        
        #Se imprime el nombre de la carpeta creada y la cantidad de archivos
        print(f"Folder '{folder}' created with 10 files.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_folder()

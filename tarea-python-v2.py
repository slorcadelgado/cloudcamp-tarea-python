import os
import shutil
import uuid
from datetime import datetime

FOLDER_NAME_FILE = "last_folder.txt"

def get_previous_folder_name():
    if os.path.exists(FOLDER_NAME_FILE):
        with open(FOLDER_NAME_FILE, "r") as f:
            return f.read().strip()
    return None

def save_folder_name(folder_name):
    with open(FOLDER_NAME_FILE, "w") as f:
        f.write(folder_name)

def create_folder():
    try:
        #Leer el nombre anterior de la carpeta
        previous_folder = get_previous_folder_name()
        if previous_folder and os.path.exists(previous_folder):
            shutil.rmtree(previous_folder)
            print(f"Previous folder '{previous_folder}' deleted.")

        #Crear nuevo nombre de carpeta con UUID
        folder = f"folder_{uuid.uuid4()}"
        os.makedirs(folder)
        print(f"New folder '{folder}' created.")

        #Guardar el nuevo nombre de la carpeta en el archivo
        save_folder_name(folder)

        #Crear 10 archivos dentro de la carpeta
        for i in range(1, 11):
            file_name = f"file_{i}.txt"
            route = os.path.join(folder, file_name)
            with open(route, "w") as file:
                date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                file.write(f"Date and Time: {date_time}")
                file.close()

        print(f"Folder '{folder}' created with 10 files.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_folder()


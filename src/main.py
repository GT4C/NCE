import os
import shutil
import re

def rename_and_move_zip(new_name: str) -> None:

    source_folder = '/home/mariot/NCE/origen/'

    destination_folder = '/home/mariot/NCE/destino'


    # Expresión regular para encontrar el archivo con el formato correcto
    pattern = re.compile(r"The_WDM_service_configuration_table_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.zip")
    
    try:
        # Buscar el archivo en la carpeta de origen
        files = os.listdir(source_folder)
        zip_file = next((f for f in files if pattern.match(f)), None)

        if not zip_file:
            print("No se encontró un archivo con el formato esperado en la carpeta origen.")
            return

        # Construir nuevo nombre del archivo reemplazando la parte inicial
        date_part = zip_file[len("The_WDM_service_configuration_table_"):-4]  # Extrae la parte de la fecha y hora
        new_filename = f"{new_name}_table_{date_part}.zip"

        # Rutas completas
        old_path = os.path.join(source_folder, zip_file)
        new_path = os.path.join(destination_folder, new_filename)

        # Renombrar y mover el archivo
        shutil.move(old_path, new_path)
        print(f"Archivo renombrado a {new_filename} y movido a {destination_folder}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == '__main__':
    
    rename_and_move_zip('Acaponeta 2')
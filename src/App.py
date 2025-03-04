import os
import shutil
import re

def mover_y_renombrar_zip(nuevo_prefijo):

    carpeta_origen="origen"

    carpeta_sitios="sitios"

    # Verifica si la carpeta origen existe y tiene archivos
    archivos = os.listdir(carpeta_origen)
    if not archivos:
        print(f"No hay archivos en la carpeta '{carpeta_origen}'.")
        return
    
    archivo = archivos[0]  # Como siempre es un solo archivo, lo tomamos directamente
    patron = re.match(r"Manage_WDM_Trail_(\d{4}-\d{2}-\d{2}_\d+-\d+-\d+)\.zip", archivo)
    
    if patron:
        nueva_nomenclatura = f"{nuevo_prefijo}_{patron.group(1)}.zip"
        ruta_original = os.path.join(carpeta_origen, archivo)
        ruta_nueva = os.path.join(carpeta_sitios, nueva_nomenclatura)

        # Mueve el archivo renombrado a la carpeta sitios (lo elimina de origen automáticamente)
        shutil.move(ruta_original, ruta_nueva)
        print(f"Archivo renombrado y movido: {ruta_original} -> {ruta_nueva}")
    else:
        print(f"El archivo '{archivo}' no cumple con la nomenclatura esperada.")


import pysftp
import dotenv
import os
import zipfile

# Cargar variables de entorno
dotenv.load_dotenv()

# Credenciales de conexión SFTP
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

sftp_config = {
    "host": host,
    "username": user,
    "password": password
}

# Rutas
local_folder = "/home/mariot/Downloads/"  # Carpeta donde se encuentran los archivos ZIP
extracted_folder = "/home/mariot/Downloads/extracted/"  # Carpeta para los archivos descomprimidos
remote_folder = "/backup/test/"  # Carpeta remota en el servidor SFTP

# Función para descomprimir un archivo ZIP
def extract_zip(zip_path, extract_to):
    print(f"Descomprimiendo el archivo: {zip_path} en {extract_to}...")
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)  # Crear la carpeta si no existe
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Archivos descomprimidos en: {extract_to}")

# Función para descomprimir todos los archivos .zip en la carpeta local
def extract_all_zips(folder, extract_to):
    print(f"Buscando archivos .zip en la carpeta: {folder}")
    zip_files = [f for f in os.listdir(folder) if f.endswith(".zip")]

    if not zip_files:
        raise FileNotFoundError("No se encontró ningún archivo .zip en la carpeta especificada.")

    print(f"Archivos .zip encontrados: {zip_files}")
    for zip_file in zip_files:
        zip_path = os.path.join(folder, zip_file)
        extract_zip(zip_path, extract_to)
    print("Todos los archivos .zip han sido descomprimidos.")

# Función para enviar todo el contenido de una carpeta al servidor SFTP
def send_to_sftp():
    try:
        print("Iniciando conexión al servidor SFTP...")
        with pysftp.Connection(**sftp_config) as sftp:
            print("Conexión establecida con el servidor SFTP.")

            # Verificar si la carpeta remota existe
            print(f"Verificando si la carpeta remota '{remote_folder}' existe...")
            if not sftp.exists(remote_folder):
                raise FileNotFoundError(f"La carpeta remota '{remote_folder}' no existe.")
            else:
                print(f"La carpeta remota '{remote_folder}' existe.")

            # Descomprimir todos los archivos ZIP
            extract_all_zips(local_folder, extracted_folder)

            # Subir los archivos descomprimidos al servidor
            print(f"Subiendo archivos descomprimidos desde {extracted_folder} a {remote_folder}...")
            for file in os.listdir(extracted_folder):
                local_file_path = os.path.join(extracted_folder, file)
                remote_file_path = os.path.join(remote_folder, file)
                if os.path.isfile(local_file_path):  # Asegurarse de que es un archivo
                    print(f"Subiendo archivo: {local_file_path} a {remote_file_path}")
                    sftp.put(local_file_path, remote_file_path)
                    print(f"Archivo '{file}' subido exitosamente.")
            print("Todos los archivos se subieron correctamente.")
    except Exception as e:
        print(f"Error durante la transferencia: {e}")


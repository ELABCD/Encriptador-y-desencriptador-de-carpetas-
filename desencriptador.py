import os
from cryptography.fernet import Fernet

def load_key(filename):
    """Carga la clave desde un archivo."""
    with open(filename, 'rb') as key_file:
        return key_file.read()

def decrypt_file(file_path, key):
    """Desencripta un archivo y lo guarda como un nuevo archivo sin la extensión .enc."""
    fernet = Fernet(key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted_data)
    
    # Guardar el archivo desencriptado
    decrypted_file_path = file_path[:-4]  # Remueve la extensión .enc
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"Archivo desencriptado: {decrypted_file_path}")

    # Borrar el archivo encriptado
    os.remove(file_path)
    print(f"Archivo encriptado borrado: {file_path}")

def decrypt_folder(folder_path):
    """Desencripta todos los archivos en la carpeta especificada que tienen la extensión .enc."""
    key = load_key('clave.key')  # Carga la clave desde el archivo
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if filename.endswith('.enc') and os.path.isfile(file_path):  # Asegurarse de que sea un archivo encriptado
            decrypt_file(file_path, key)

    print("Todos los archivos encriptados en la carpeta han sido desencriptados.")

if __name__ == "__main__":
    folder_path = r"Ruta Del Archivo Encriptado Que Quieras Desencriptar!"  # Cambia esto a la ruta de tu carpeta

    # Verifica si la carpeta existe
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print("La carpeta existe. Procediendo a desencriptar...")
        decrypt_folder(folder_path)
    else:
        print("La carpeta especificada no existe. Por favor, verifica la ruta.")

import os
from cryptography.fernet import Fernet

def generate_key():
    """Genera una clave y la devuelve."""
    return Fernet.generate_key()

def save_key(key, filename):
    """Guarda la clave en un archivo."""
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    """Encripta un archivo y lo guarda como un nuevo archivo con la extensión .enc."""
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    
    # Guardar el archivo encriptado con .enc
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"Archivo encriptado: {encrypted_file_path}")

    # Borrar el archivo original
    os.remove(file_path)
    print(f"Archivo original borrado: {file_path}")

def encrypt_folder(folder_path):
    """Encripta todos los archivos en la carpeta especificada."""
    key = generate_key()
    save_key(key, 'clave.key')  # Guarda la clave en un archivo

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):  # Asegurarse de que sea un archivo
            encrypt_file(file_path, key)

    print("Todos los archivos encriptados en la carpeta.")

if __name__ == "__main__":
    folder_path = r"Ruta Del Archivo Que Quieras Encriptar!"  # Cambia esto a la ruta de tu carpeta

    # Verifica si la carpeta existe
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        encrypt_folder(folder_path)
    else:
        print("La carpeta especificada no existe.")

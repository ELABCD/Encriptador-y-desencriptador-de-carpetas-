Encriptador y Desencriptador de Carpetas

Este repositorio contiene dos scripts de Python que permiten encriptar y desencriptar todos los archivos dentro de una carpeta específica. Utiliza la biblioteca cryptography para garantizar la seguridad de los datos mediante encriptación simétrica con Fernet.

Funcionalidades:

    Encriptador (encriptador.py):
        Genera una clave de encriptación usando Fernet.
        Guarda la clave en un archivo llamado clave.key.
        Encripta todos los archivos dentro de una carpeta especificada.
        Almacena los archivos encriptados con una extensión .enc.
        Elimina los archivos originales después de haber sido encriptados, para asegurar que solo se conserven los archivos encriptados.

    Desencriptador (desencriptador.py):
        Carga la clave de encriptación desde el archivo clave.key.
        Desencripta todos los archivos dentro de la carpeta que tienen la extensión .enc.
        Restaura los archivos desencriptados a su estado original, eliminando la extensión .enc.
        Borra los archivos encriptados después de que se han desencriptado, para evitar conservar datos encriptados innecesarios.

Uso:

    Requisitos:
        Python 3.x
        Biblioteca cryptography (puedes instalarla usando pip install cryptography)

    Ejemplo de Ejecución:
        Para encriptar archivos en la carpeta Hola, asegúrate de que la carpeta existe y ejecuta el script encriptador.py.
        Para desencriptar los archivos encriptados en la misma carpeta, ejecuta el script desencriptador.py.

Notas Importantes:

    Seguridad: Mantén la clave clave.key en un lugar seguro, ya que es necesaria para desencriptar los archivos.
    Precaución: Este script eliminará los archivos originales después de encriptarlos y los archivos encriptados después de desencriptarlos. Asegúrate de tener copias de seguridad si es necesario.

    Espero que les guste es algo basico! :D

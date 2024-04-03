import os

try:
    # Solicitar al usuario que ingrese el nombre del archivo de texto
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

    # Obtener la ruta absoluta del archivo de texto en la misma carpeta que el script
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    # Abrir el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        
        # Dividir el contenido en palabras
        palabras = contenido.split()
        
        # Contar el número de palabras
        numero_palabras = len(palabras)
        
        # Imprimir el resultado
        print("El número de palabras en el archivo es:", numero_palabras)
        
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print("Ocurrió un error:", e)

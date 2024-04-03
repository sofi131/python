import os

try:
    # Solicitar al usuario que ingrese la ruta completa del archivo de texto
    ruta_archivo = input("Ingrese la ruta completa del archivo de texto: ")

    # Verificar si la ruta de archivo es válida
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta especificada: {ruta_archivo}")

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
        
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Ocurrió un error:", e)

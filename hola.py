def contar_vocales(frase):
    # Inicializamos un contador para vocales
    vocales = 0
    
    # Convertimos la cadena a minúsculas para simplificar la comparación
    frase = frase.lower()
    
    # Definimos las vocales
    vocales_lista = ['a', 'e', 'i', 'o', 'u']
    
    # Iteramos sobre cada carácter en la cadena
    for caracter in frase:
        # Si el carácter es una vocal, aumentamos el contador de vocales
        if caracter in vocales_lista:
            vocales += 1
    
    return vocales

def contar_consonantes(frase):
    # Inicializamos un contador para consonantes
    consonantes = 0
    
    # Convertimos la cadena a minúsculas para simplificar la comparación
    frase = frase.lower()
    
    # Definimos las vocales
    vocales_lista = ['a', 'e', 'i', 'o', 'u']
    
    # Iteramos sobre cada carácter en la cadena
    for caracter in frase:
        # Si el carácter es una letra y no es una vocal, aumentamos el contador de consonantes
        if caracter.isalpha() and caracter not in vocales_lista:
            consonantes += 1
    
    return consonantes

# Ejemplo de uso:
cadena = "Esta es una cadena de ejemplo"
vocales = contar_vocales(cadena)
consonantes = contar_consonantes(cadena)
print("Número de vocales:", vocales)
print("Número de consonantes:", consonantes)


def vocales_no_repetidas_y_cantidad(frase):
    # Utilizamos un conjunto para almacenar las vocales únicas
    vocales = {'a', 'e', 'i', 'o', 'u'}
    # Utilizamos un conjunto para almacenar las vocales encontradas en la frase
    vocales_encontradas = {caracter for caracter in frase.lower() if caracter in vocales}
    # Devolvemos las vocales no repetidas y su cantidad
    return vocales_encontradas, len(vocales_encontradas)

# Ejemplo de uso:
cadena = "Esta es una frase con vocales"
vocales, cantidad = vocales_no_repetidas_y_cantidad(cadena)
print("Vocales no repetidas:", vocales)
print("Cantidad de vocales no repetidas:", cantidad)




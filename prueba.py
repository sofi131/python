# Función para comprobar si una palabra es un palíndromo
def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Verificar si la palabra es un palíndromo
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

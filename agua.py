#https://www.codewars.com/kata/575fa9afee048b293e000287

def cuanta_agua_necesaria(agua, carga, ropa):
    if ropa < carga:
        return 'No hay suficiente ropa'
    elif ropa > 2 * carga:
        return 'Demasiada ropa'
    else:
        agua_necesaria = agua * (1.1 ** (ropa - carga))
        return round(agua_necesaria, 2)

# Ejemplo de uso:
print(cuanta_agua_necesaria(5, 10, 14))  # Output esperado: 7.89


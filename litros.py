#https://www.codewars.com/kata/57b58827d2a31c57720012e8
def calcular_costo_total(litros, precio):
    descuento_total = min(25, (litros // 2) * 5)
    costo_sin_descuento = litros * precio
    costo_con_descuento = costo_sin_descuento - (descuento_total / 100)
    return round(costo_con_descuento, 2)

# Solicitar la entrada de litros y precio fuera de la función
litros = int(input("Ingrese la cantidad de litros comprados: "))
precio = float(input("Precio por litro: "))  # Utiliza float para permitir precios con decimales

# Llama a la función con los valores proporcionados por el usuario
costo_total = calcular_costo_total(litros, precio)
print("El costo total es:", costo_total, "euros")




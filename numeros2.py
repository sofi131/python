def maximo(list):
    return max(list)

def minimo(list):
    return min(list)

def contarNumeros(list):
    repeticiones={}
    for i in list:
        if i in repeticiones:
            repeticiones[i]=+1
        else:
            repeticiones[i]=1

    return repeticiones

numeros = []
for i in range(10):
    numeros.append(int(input(f"Dime un número {i}: ")))

print(maximo(numeros))
print(minimo(numeros))
print(contarNumeros(numeros))

def mostrar_fichas_dominó():
    for i in range(7):
        for j in range(i, 7):
            print(f'[{i}|{j}]', end=' ')
        print()

# Llamada a la función para mostrar las fichas del dominó
mostrar_fichas_dominó()

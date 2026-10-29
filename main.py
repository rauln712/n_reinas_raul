
reinas = []

def imprimir_tablero(reinas, n):
    for fila in range(n):
        for columna in range(n):
            if fila < len(reinas) and reinas[fila] == columna:
                print("♛", end=" ")
            else:
                print("·", end=" ")
        print()  # Salto de línea al terminar la fila
        
    print("-" * (2 * n))
    input("Presiona Enter para continuar...")  # Pausa para ver el tablero
def es_valida(reinas, filas, columnas):
    for i in range(len(reinas)):
        if reinas[i] == columnas or abs(reinas[i] - filas) == abs(i - columnas):
            return False
    return True


def backtracking(reinas, n):
    if len(reinas) == n:
        print("¡Solución encontrada!")
        imprimir_tablero(reinas, n)
        return

    fila = len(reinas)

    for columna in range(n):
        if es_valida(reinas, fila, columna):
            reinas.append(columna)

            print(f"Colocamos reina en fila {fila}, columna {columna}")
            imprimir_tablero(reinas, n)

            backtracking(reinas, n)

            reinas.pop()

            print(f"Retiramos reina de fila {fila}, columna {columna}")
            imprimir_tablero(reinas, n)

backtracking(reinas, 4)
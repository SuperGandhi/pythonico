def encontrar_numero_menor(lista):
    if not lista:
        return None  # Retorna None si la lista está vacía
    else:
        return min(lista)

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamada a la función
resultado = encontrar_numero_menor(mi_lista)

# Imprimir el resultado
print(f"El número menor en la lista es: {resultado}")

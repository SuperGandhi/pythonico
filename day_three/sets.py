"""
Práctica Sets 1 Une los siguientes sets en uno solo, llamado mi_set_3: {1, 2, "tres", "cuatro"} {"tres", 4, 5} mi_set_1 = {1, 2, "tres", "cuatro"} mi_set_2 = {"tres", 4, 5}

"""

mi_set_1 = {1, 2, "tres", "cuatro"} 
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

"""
Práctica Sets 2 Elimina un elemento al azar del siguiente set, utilizando métodos de sets. sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

"""
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.pop())

"""
Práctica Sets 3 Agrega el nombre Damián al siguiente set, utilizando métodos de sets: sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

"""

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damian")
print(sorteo)






"""
   Práctica Enumerador 1 Imprime en pantalla frases como la siguiente: '{nombre} se encuentra en el índice {indice}' Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate(). lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"] Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales. Tip: utiliza loops! lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"] print(f'{nombre} se encuentra en el índice {indice}')

"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

"""

   Práctica Enumerador 2 Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python". Llama a la lista obtenida con el nombre de variable lista_indices . "Python"

"""


lista_indices = "Python"
for indice,elemento in enumerate(lista_indices):
   print(f'{indice} -> {elemento}')    

"""

   Práctica Enumerador 3 Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M: lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"] Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos: Loops Condicionales if El método enumerate() Métodos de strings o indexado lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,nombres in enumerate(lista_nombres):
    if nombre.startswith("M"):
       print(f'Only the next names in the index ubication empty with M : {index}')

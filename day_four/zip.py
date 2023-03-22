"""
   Práctica Zip 1 Muestra en pantalla frases como la del siguiente ejemplo: "La capital de Alemania es Berlín" Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente. capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"] paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

"""

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

phrase = list(zip(capitales,paises))

for capitales,paises in phrase:
    print(f'The capital of {paises} is {capitales}')


"""
   Práctica Zip 2 Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip. marcas = productos =

"""

brands = ['Apple', 'Microsoft', 'Ibm', 'Nvidia']
products = ['Iphone', 'Office', 'Cuantic Computers', 'Graphics Card']


mixin_list_brands_products = zip(brands, products)

for tuple in mixin_list_brands_products:
    print(tuple)

"""
   Práctica Zip 3 Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros: uno / um / one dos / dois / two tres / três / three cuatro / quatro / four cinco / cinco / five El resultado deberá seguir la estructura: [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ] 1: uno / um / one 2: dos / dois / two 3: tres / três / three 4: cuatro / quatro / four 5: cinco / cinco / five

"""


numbers_spanish = "uno", "dos", "tres", "cuatro", "cinco"
numbers_portuguese = "um", "dois", "três", "quatro", "cinco" 
numbers_english = "one", "two", "three", "four", "five"

numbers = list(zip(numbers_spanish, numbers_portuguese, numbers_english))

for number_spanish,numbers_portuguese,numbers_english in numbers:
    print(numbers) 

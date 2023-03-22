"""
   Práctica Zip 1 Muestra en pantalla frases como la del siguiente ejemplo: "La capital de Alemania es Berlín" Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente. capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"] paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

"""

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

phrase = list(zip(capitales,paises))

for capitales,paises in phrase:
    print(f'The capital of {paises} is {capitales}')
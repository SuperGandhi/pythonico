"""
Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente

"""

def potencia(base, exponente):
    return base ** exponente

print(potencia(2,4))



"""

Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.85 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.


"""

def usd_a_eur(dollar):
   return dollar *  0.85

dollar = usd_a_eur(50)
print(dollar)


"""

Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

"""

def word_reverse(word):
    reverse_word = word[::-1].upper()
    return reverse_word
      

palabra = word_reverse("hola")
print(palabra)






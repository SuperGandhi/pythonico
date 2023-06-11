from Aritmetics_operations import sum_rest
from Aritmetics_operations.Formulas import geometrics_formulas

sum = sum_rest.suma(12,23)
rest = sum_rest.rest(23,34)
circle_radio = geometrics_formulas.circle_radio(10)
perimeter_triangle = geometrics_formulas.perimeter_triangle(2,3,4)

print(f"The circle radio is: {circle_radio} and the perimeter triangle is: {perimeter_triangle}")

print(f"Sum resul is: {sum} and rest result is : {rest}")  
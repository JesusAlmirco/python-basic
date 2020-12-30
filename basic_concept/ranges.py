"""
Se puede crear una lista de numeres automaticamente
usando la palabra reservada "range"
For example:
"""
range_number = list(range(0, 100))
print("Rango de numeros de 0 a 100: ", range_number, "es de tipo ", type(range_number))

#Example de numeros impares
impar = list(range(1, 100, 2))
print("Numeros impares de 1 a 100: ", impar, "es de tipo ", type(impar))
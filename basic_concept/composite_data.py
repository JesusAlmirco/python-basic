#Los datos compuestos son aquellos que estan echos de diferentes objetos.
#Se pueden almacenar varios objetos

#Listas -> establecemos una variables y los valores de colocan entre corchetes []
student_grades = [19, 15, 18, 14, 17, 16, 13]
print("Numero de valores existentes: ", len(student_grades))
print("Las notas varian entre: ", student_grades[4], "es de tipo ", type(student_grades))
print("Las notas varian entre: ", student_grades[0:5])
print("Las notas varian entre: ", student_grades[-4])
#Tuplas -> establecemos una variables y los valores de colocan entre parentesis ()
worker = (2020333, "Obregon Almirco", "Jesus")
print()
#Diccionarios -> establecemos en una variables y los valores de colocan entre llaves {}
year = {
    "Jan": 1500,
    "Feb": 2860,
    "Mar": 1597,
}
print("Los valores de la variable son: ", year, "es de tipo ", type(year))
print("Uno de los meses del year", year["Mar"])

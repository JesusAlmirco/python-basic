#Los datos compuestos son aquellos que estan echos de diferentes objetos.
#Se pueden almacenar varios objetos

#Listas -> establecemos una variables y los valores de colocan entre corchetes [] y se 
#pueden modificar y agregar mas valores con el key word "append"
student_grades = [19, 15, 18, 14, 17, 16, 13]
sum_prom = sum(student_grades)
length = len(student_grades)
prom = sum_prom/length
print("El promedio de notas es: ", prom)
print("Numero de valores existentes: ", len(student_grades))
print("Las notas varian entre: ", student_grades[4], "es de tipo ", type(student_grades))
print("Las notas varian entre: ", student_grades[0:5])
print("Las notas varian entre: ", student_grades[-4])
#Tuplas -> establecemos una variables y los valores de colocan entre parentesis () no se puede
#agregar o modificar valores
worker = (2020333, "Obregon Almirco", "Jesus")
print("The solved is: ", worker, "is of type ", type(worker))
monday_temperatures = (10, 13.5, 22, 28)

#Diccionarios -> establecemos en una variables y los valores de colocan entre llaves {}
student_grade = {
    "Jany": 15,
    "Feby": 17,
    "Mary": 19,
}
mysum = sum(student_grade.values())
length2 = len(student_grade)
mean = mysum/length2
print("EL promedio de notas es de: ", mean)
print("Los valores de la variable son: ", student_grade, "es de tipo ", type(student_grade))
print("La nota de Mry es de: ", student_grade["Mary"])

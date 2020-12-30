def mean(mylist):
    """
    docstring
    """
    the_mean = sum(mylist)/len(mylist)
    return the_mean

print(mean([10, 8.8, 7.8, 9, 5.5, 7]), "es de tipo ", type(mean))


def price(lins):
    current_value = 49.7434
    maped = lins/current_value
    return maped

print("The price is: ", price(4000))

def edad():
    """
    docstring
    """
    my_year = int(input("Ingrese tu edad: "))
    
    if my_year<18:
        print("No eres menor de edad. ")
    else:
        print("Ya eres mayor de dad")
        
print(edad)
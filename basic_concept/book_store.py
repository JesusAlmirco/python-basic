print("*********Proporcione los siguientes Datos*********")
name = input("Enter Book Name: ")
book_id = int(input("Enter Book ID: "))
book_price = float(input("Enter Book Price: "))
free_delivery = input("Book delivery FREE? (True/False): ")

if free_delivery == "True":
    free_delivery = True
elif free_delivery == "False":
    free_delivery = False
else:
    free_delivery = "Incorrect Value, only will be (True or False)"

print("-----------------------------------")
print("Book name is: ", name)
print("Book ID is: ", book_id)
print("Book price is: ", book_price)
print("Free Delivery: ", free_delivery)

print("****Program End*********")
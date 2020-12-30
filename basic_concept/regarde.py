#name = str(input("Enter your name: "))
#string formats
#message = "Hello %s" % name #Available for python2 and python3
#New string format in python3.6
# message = f"Hello {name}"
# print("Hello", message)

def regard(person_name):
    message = "Hi, " + person_name
    return message
   
print(regard("Mary"))

colors = [11, 34, 98, 43, 45, 54, 54]
for greater in colors:
    if greater > 50:
        print(greater)
import json

#Declarate parameter for load file "data.json"
data = json.load(open("data.json"))

#Function for search the word in data.json
def translate(w):
    
    w = w.lower()
    
    #Interate on data file for search the word definition
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."
    
#Input word by terminal
input_word = input("Enter word: ")

print(translate(input_word))
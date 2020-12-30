print("***********TextPro Builder**************")

def text_make(sentence):
    interrogatives = ("how", "what", "why")
    capitalized = sentence.capitalize()
    
    if sentence.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
text = []

while True:
    text_input = input("Say Something: ")
    if text_input == "q":
        break
    else:
        text.append(text_make(text_input))
        
print(" ".join(text))
    
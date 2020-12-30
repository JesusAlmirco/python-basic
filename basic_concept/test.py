# myfile = open('text.tx')
# content = myfile.read()
# myfile.close()

#**********open files with keyword "with"**********
# with open('files/text.txt') as myfile:
#     content = myfile.read()
   # myfile.close() - close not necesary
#print(content)   
   
#******Create new file 
# with open("files/fruit.text", 'w') as myfile:
#     myfile.write("Writing new text with python\nthis is new for me\nPython is fantastic")


#******print numbers of occurrences in text file *****
# def foo(character, filepath="bear.txt"):
#     my_file = open('bear.txt')
#     text_content = my_file.read()
    #the keyword "count() imprimer cuantas veces se repite un dato"
    #return text_content.count(character)
    
with open('file.txt', 'w') as my_file:
    my_snail = my_file.write("snail")
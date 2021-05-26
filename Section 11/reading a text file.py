myfile = open("Section 11/fruits.txt")
content = myfile.read()
print(content)
myfile.close() # not mandatory but recomended

# another method to do so
# with manager will close the file automatically
# "r" for reading, "w" for writing
# "w" will create the file if it doesn't exist / if exist python will override
# with open("file.txt","w") as file:
#     file.write("snail")
with open("Section 11/fruits.txt", "r") as myfile:
    content = myfile.read()
print(content)

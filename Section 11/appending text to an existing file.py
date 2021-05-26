# x will check if the file exists
    # with open("Section 11/fruits.txt", "x") as file:
    #     file.write("Okra")
# a will append
with open("Section 11/fruits.txt", "a") as file:
    file.write("\nOkra")
# once the code append something to the text the cusrsor will go at the end, 
    file.seek(0)
# seek(0) will take the control to 0th position, so
    content = file.read()
# will work and gives an output of the whole text, since the cursor is at the 0th position.
print(content)


# You can both append and read a file with:

# with open("file.txt", "a+") as file:
#     content = file.write("Even more sample text")
#     file.seek(0)
#     content = file.read()



# not all the python builtin modules are built in C language, 
# there is builtin modules which are built in python
# these modules are cannot be imported using import sis, it can be imported using 
#>>> import os
#>>> sys.prefix 
# this will give you the location of python installed
#>>> dir(os) 
# this will give you the components of os module
#>>> os.path.exists("vegetables.txt")
# this wil check if the file exist in that given path, if not this will return false otherwise true


import os
import time
while True:
    if os.path.exists("Modules/vegetables.txt"):
        with open("Modules/vegetables.txt") as file:
            print(file.read())
    else:
        print("file does not exist")
    time.sleep(10)


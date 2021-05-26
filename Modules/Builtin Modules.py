# not all functions are imported in to python interpreter software when it installed
# so have to import some
#>>> import sys - sys means system
# to see the list builtin modules =>
#>>> sys.builtin_module_names
# to use any of the module simply import the module name for example
#>>> import time
# this will import the builtin module time for us to use
#>>> dir(time)
# this will help to see the properties of time for us to use
#>>> time.sleep(3)
# this will put the process in sleep for 3 seconds


import time
 while True:
     with open("vegetables.txt") as file:
         print(file.read())
         time.sleep(10)

# this while loop will work every 10 seconds 



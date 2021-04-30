student_grades = {"Mary": 9.1, "Sim": 8.8, "John":7.5} 

# >>> student_grade[1]
# KeyError: 1 // because the dictionary does'nt have key called 1

# >>> student_grades["Sim"]
# 8.8
# >>> # will work because dictionary have key called Sim

# Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

# From tuple to list:
# >>> data = (1, 2, 3)
# >>> list(data)
# [1, 2, 3]

# From list to tuple:
# >>> data = [1, 2, 3]
# >>> tuple(data)
# (1, 2, 3)

# From list to dictionary:
# >>> data = [["name", "John"], ["surname", "smith"]]
# >>> dict(data)
# {'name': 'John', 'surname': 'smith'}
# Note that the original data type needs to have the data structured in a way that can be understood by the new data type. For example, the following would not work:

# >>> data = [1, 2, 3]
# >>> dict(data)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
# That's because a dictionary is made of key and value pairs, but the list was not constructed that way, so the above would generate an error.


####                 Summary: Positive/Negative Indexes, Slicing                 ####
####                 In this section, you learned that:                          ####

# Lists, strings, and tuples have a positive index system:
# ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#    0      1      2      3      4      5      6

# And a negative index system:
# ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#   -7     -6     -5     -4     -3     -2     -1

# In a list, the 2nd, 3rd, and 4th items can be accessed with:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[1:4]
# Output: ['Tue', 'Wed', 'Thu']

# First three items of a list:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[:3]
# Output:['Mon', 'Tue', 'Wed'] 

# Last three items of a list:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[-3:]
# Output: ['Fri', 'Sat', 'Sun']

# Everything but the last:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[:-1] 
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

# Everything but the last two:
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[:-2] 
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

# A single in a dictionary can be accessed using its key:
# phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
# phone_numbers["Marry Simpsons"]
# Output: '+423998200919'
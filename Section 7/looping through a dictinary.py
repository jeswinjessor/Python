student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
# for dictionary specify wether item, key or values
for grade in student_grades.items():
    print(grade)
# output will be in tuples
#('Mary', 9.1)
#('Sim', 8.8)
#('John', 7.5)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print(value.replace('+', '00'))
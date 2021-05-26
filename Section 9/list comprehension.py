temps = [221, 234, 340, 230]

# an inline for loop
new_temps = [temp / 10 for temp in temps]

# an inline for loop including an if statements
new_temps = [temp / 10 for temp in temps if temp != -9999]

# if it is if-else statement then
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]


print(new_temps)
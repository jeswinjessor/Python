monday_temperature = [9.1,8.8,7.5,6.6,9.9]

#monday_temperature.index(8.8) => will give you the index number of the system

# >>> dir(list) => will give you the directory of list 

#monday_temperature.__getitem__(1) => will give you 8.8 ## don't use this ugly metgod

#SHOULD USE THIS
# monday_temperature[1] => will do the work

###               SLICES              ###

# monday_temperature[1:4]
# Result will be => [8.8,7.5,6.6]

# to get first two item of list
# monday_temperature[0:2]
# result will be => [9.1,8.8]
#              => SHORTCUT <=
#   monday_temperature[:2]

# to get the last two item of list
# monday_temperature[3:5]
# result will be => [6.6, 9.9]
#              => SHORTCUT <=
#   monday_temperature[3:]

# to get an item with an index
# monday_temperature[4]
# result will be => 9.9

# to get the last item of the list
# monday_temperature[-1]
# result will be => 9.9

#to get third last item of the list
# moday_temperature[-3]  

# to get last two item
# monday_temperature[-2:]
# result will be => [6.6, 9.9]

# to slice an element
# >>> monday_temperature = ['hello', 1,2,3]
# >>> monday_temperature[0]
# 'hello'
# >>> monday_temperature[0][2]
# 'l'


